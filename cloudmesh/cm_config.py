import yaml
import os
import json

class cm_config:

	default_path = '.futuregrid/cloudmesh.yaml'
	filename = ""
	data = {}
	
	def __init__ (self, filename=None):
		if filename == None:
			home = os.environ['HOME']
			self.filename = "%s/%s" % (home, self.default_path)
		else:
			self.filename = filename
		self.read(self.filename)
		return

	def read(self, filename):
		self.filename = filename
		f = open(self.filename, "r")
		self.data = yaml.safe_load(f)
		f.close()

	def __str__(self):
		return json.dumps(self.data, indent=4)

	def write(self, filename):
		""" BUG DOES NOT WORK"""
		f = open(filename, "w")
		yaml.dump(self.data, f, default_flow_style=False, indent=4)
		f.close()

	def default(self):
		return self.data['default']

	def get(self, key=None):
		if key == None:
			return self.data['cloudmesh']
		else:
			return self.data['cloudmesh'][key]

	def keys(self):
		return self.data['cloudmesh'].keys()

	def rc(self, name):
		result = self.get(name)
		lines = ""
		for (attribute, value) in result.iteritems():
			lines += "export %s=%s" % (attribute, value)
			lines += "\n"
		return lines

if __name__ == "__main__":
    config = cm_config()

    print config

    print "================="
    print config.get('india-openstack')
    print "================="
    print config.get()
    print "================="
    print config.keys()
    print "================="
    print config.rc('india-openstack')
    print "================="
    print config.default()
    print "================="
    outfile = "%s/%s" %( os.environ['HOME'], ".futuregrid/junk.yaml")
    print config.write(outfile)
    os.system("cat " + outfile)
