Python Script to extract following information from PDB File (Download PDB file with ID '2wsc' from RCSB protein data bank www.rcsb.org )

	- Title/Name  of the protein.
	- Total length of the protein/ number of residues in the given pdb 
	- No of chains present in protein and their names(Ascending order if chains are named numerically followed by alphabetical order)
	- All aminoacid ratios present in the protein in alphabetical order.
		ex: Ratio(Leu) = no of leucine present/total length of protein.
	- Are there any unknown aminoacids present ? If so, mention total count.
	- Are there any ligand molecules other than water ? If so, mention their names.
	- Calculate all possible phi, psi, omega angles for the given pdb.

Output file :

line_no		Description
- 1		Title or name --- (CRYSTAL STRUCTURE OF ENZYME COMPLEXED WITH LIGANDS)
- 2		length of protein --- (LENGTH(\t)472)
- 3		no of chains in protein and names arranged in order --- (CHAINS(\t)4(\t)1,A,B,C) --- Names separated by comma(',')
- 4-22		Aminoacid ratios --- (ALA(\t)0.125874125874)
- 23		unknown aminoacids count --- (UNKNOWN('\t')0)
- 24		ligands if any --- (LIGANDS(\t)5JN,CAC,HEM,NO,NO3,RQ3) --- Names separated by comma(',')
- 25		chain name --- (CHAIN-1)
- 26		possible phi,psi,omega angles --- (NA('\t')-21.55049('\t')-45.13716)	
- 27		possible phi,psi,omega angles
- 28		possible phi,psi,omega angles
- 29-32		same as 25-28
- 33-36		same as 25-28
- 37-40		same as 25-28

 ('NA' if calculation of respective torsion angle is not possible.)

