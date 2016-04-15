import sys
import math
temp1 = {}
chains = {}
amino = {}
lig = {}
angles = []
ang_pos = 0
temp2 = {}
def calculate_dihedral_angle(a,b, c, d,check):

					a1 = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
					a2 = (c[0] - b[0], c[1] - b[1], c[2] - b[2])
					a3 = (d[0] - c[0], d[1] - c[1], d[2] - c[2])
					b1 = a1[1]*a2[2] - a1[2]*a2[1]
					b2 = a1[2]*a2[0] - a1[0]*a2[2]
					b3 = a1[0]*a2[1] - a1[1]*a2[0]
					n1 = (b1, b2, b3)
					b1 = a2[1]*a3[2] - a2[2]*a3[1]
					b2 = a2[2]*a3[0] - a2[0]*a3[2]
					b3 = a2[0]*a3[1] - a2[1]*a3[0]

					n2 = (b1, b2, b3)
					unit_n1 = math.sqrt(math.fabs(n1[0] * n1[0]) + math.fabs(n1[1] * n1[1]) + math.fabs(n1[2] * n1[2]) )
					n1 = (n1[0]/unit_n1, n1[1]/unit_n1, n1[2]/unit_n1)
					unit_n2 = math.sqrt(math.fabs(n2[0] * n2[0]) + math.fabs(n2[1] * n2[1]) + math.fabs(n2[2] * n2[2]) )
					n2 = (n2[0]/unit_n2, n2[1]/unit_n2, n2[2]/unit_n2)
					modb2 = math.sqrt(math.fabs(a2[0] * a2[0]) + math.fabs(a2[1] * a2[1]) + math.fabs(a2[2] * a2[2]) )
					a2 = (a2[0]/modb2, a2[1]/modb2, a2[2]/modb2)
					b1 = n1[1]*a2[2] - n1[2]*a2[1]
					b2 = n1[2]*a2[0] - n1[0]*a2[2]
					b3 = n1[0]*a2[1] - n1[1]*a2[0]
					m1 = (b1,b2,b3)
					ans1 = n1[0]*n2[0] + n1[1]*n2[1] + n1[2]*n2[2]
					ans2 = m1[0]*n2[0] + m1[1]*n2[1] + m1[2]*n2[2]
					temp=180/math.pi
					final_ans= math.atan2(ans2, ans1) * temp 


					return final_ans

no_of_acid = 0
unknown_count = 0
angle_num = 0


##### We INITIALZE THE DATA STRUCTURES NECESSARY ###############

imput_file = open(sys.argv[1], 'rU')
output_file = open(sys.argv[1].split('.')[0] + '_output.txt', 'w')

the_angles = (0,0,0)
now_chain = None


temp1['N'] =  (0.0, 0.0, 0.0)
temp1['CA'] = (0.0, 0.0, 0.0)
temp1['C']  = (0.0, 0.0, 0.0)
temp2['N']  =  temp1['N'] 
temp2['CA'] =  temp1['CA'] 
temp2['C']  =  temp1['C']

inputer = imput_file.readlines()
i = -1
length=len(inputer)-1
#Start Process

while i < length:
			## READ INPUT
			i += 1
			line = inputer[i]

			#### READ THE TITLE OF FILE
			if line.startswith('TITLE'):
				name = line[5:].strip()

			#### READ THE SEQUERS	
			if line.startswith('SEQRES'):
				line_list = line.split()
				chain_name = line_list[2].strip()
				if chain_name not in chains:
					chains[chain_name] = int(line_list[3])
					no_of_acid += chains[chain_name]
				for aa in line_list[4:]:
					aa = aa.strip()
					if aa not in amino:
						amino[aa] = 0
					amino[aa] += 1

			####  READ LINE WITH 'HET'		
			if line.startswith('HET') and not line.startswith('HETATM'):
				line_list = line.split()
				ligand = line_list[1].strip()
				if ligand not in lig:
					lig[ligand] = 1



			#### CHECK THE ATOMS		
			if line.startswith('ATOM'):
							line_list = line.split()


							if line_list[4].strip() == now_chain:


										if ang_pos == 1:
											temp1['N'] = temp2['N']
											temp1['CA'] = temp2['CA']
											temp1['C'] = temp2['C']
											
											while True:
														if line.startswith('ATOM') == False or line_list[4].strip() != now_chain:
															angles.append(('s', float('nan')))
															angles.append(('o', float('nan')))
															ang_pos = (ang_pos + 2) % 3
															break
														if line_list[2].strip() == 'N':
															temp2['N'] = (float(line_list[6].strip()), float(line_list[7].strip()), float(line_list[8].strip()))
															s = calculate_dihedral_angle(temp1['N'], temp1['CA'], temp1['C'], temp2['N'],0)
															the_angles = ('s', s)
															angles.append(the_angles)
															ang_pos = (ang_pos + 1)%3
															break
														i += 1
														line = inputer[i]
														line_list = line.split()
											continue



										if ang_pos == 2:
											temp2['CA'] = (float(line_list[6].strip()), float(line_list[7].strip()), float(line_list[8].strip()))
											o = calculate_dihedral_angle(temp1['CA'], temp1['C'], temp2['N'], temp2['CA'],0)
											the_angles = ('o', o)
											angles.append(the_angles)
											ang_pos = (ang_pos + 1)%3
											continue




										if ang_pos == 0:
											temp2['C'] = (float(line_list[6].strip()), float(line_list[7].strip()), float(line_list[8].strip()))
											p = calculate_dihedral_angle(temp1['C'], temp2['N'], temp2['CA'], temp2['C'],0)
											the_angles = ('p', p)
											angles.append(the_angles)
											ang_pos = (ang_pos + 1)%3
											continue


							## FOR OTHER CASES
							else:
								now_chain = line_list[4].strip()
								temp2['N'] = (float(line_list[6].strip()), float(line_list[7].strip()), float(line_list[8].strip()))
								i += 1
								line = inputer[i]
								line_list = line.split()
								temp2['CA'] = (float(line_list[6].strip()), float(line_list[7].strip()), float(line_list[8].strip()))
								i += 1
								line = inputer[i]
								line_list = line.split()
								temp2['C'] = (float(line_list[6].strip()), float(line_list[7].strip()), float(line_list[8].strip()))
								
								the_angles = ('p', float('nan'))
								angles.append(the_angles)
								ang_pos = (ang_pos + 1)%3
								# print the_angles



### if a given acid is found to be unknown

if 'UNK' in amino:
	unknown_count = amino['UNK']
	del amino['UNK']

#GENERATING OUTPUT FILE :::::::::;


output_file.write(name + '\n')
output_file.write('LENGTH '+  str(no_of_acid)+'\n')
output_file.write('CHAINS ' + str(len(chains.keys())) +'\t' + ','.join(sorted(chains.keys())) +'\n')
no_of_acid = float(no_of_acid)


for k in sorted(amino.keys()):
	output_file.write(k + ' ' + str(amino[k]/no_of_acid) + '\n')
output_file.write('UNKNOWN ' + str(unknown_count) + '\n')
output_file.write('LIGANDS ' + ','.join(sorted(lig.keys())) + '\n')
i = 0


for k in sorted(chains.keys()):
	output_file.write('CHAIN-' + str(k) + '\n')

	while i < len(angles)-1:
		p = angles[i][1]
		s = angles[i+1][1]
		o = angles[i+2][1]
		if math.isnan(p):
			p = 'NA'
		if math.isnan(s):
			s = 'NA'
		if math.isnan(o):
			o = 'NA'
		output_file.write(str(p) + ' ' + str(s) + ' ' + str(o) + '\n')
		i += 3
		if s == 'NA' and o == 'NA':
			break


