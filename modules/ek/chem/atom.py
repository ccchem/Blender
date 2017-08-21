from ek import Vec3


# ---------------------------------------------------------------------

# Covalent radii
COV_RAD = {
	'H': 0.37,
	'C': 0.77,  'N': 0.75, 'O': 0.73,
	'Fe': 1.25
}

# Van der Waals radii
VDW_RAD = {
    'H': 1.2,
    'Li': 2.2, 'B': 1.8,  'C': 1.7,   'N': 1.6,  'O': 1.55, 'F': 1.5,
    'Na': 2.4, 'Mg': 2.2, 'Al': 2.1,  'Si': 2.1, 'P': 1.95, 'S': 1.8, 'Cl': 1.8,
    'K': 2.8,  'Ca': 2.4, 'Fe': 2.05, 'Cu': 2.0
}


# ---------------------------------------------------------------------


class Atom(Vec3):
	
	def __init__(self, symbol, x, y, z):
		Vec3.__init__(self, x, y, z)
		self.symbol = symbol

	def __str__(self):
		return "(" + self.symbol + ", " + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


# ---------------------------------------------------------------------


class Molecule:
	
	def __init__(self):
		self.atoms = []
		self.bond = []
		
	def add_atom(self, atom):
		self.atoms.append(atom)

	def read_xyz(self, filename):		
		f = open(filename)		
		
		numatoms = int(f.readline())	# number of atoms
		f.readline()					# skip comment

		for i in range(numatoms):
			tokens = f.readline().split()
			print(tokens)
		
		f.close()
		

# ---------------------------------------------------------------------

