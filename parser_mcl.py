# -*- coding:utf-8 -*-
import re,csv
import os 
r_strain = r = re.compile(r'\(.*\)')
f = open('label.tab','r')
# headline = f.readline()
label = [x.strip() for x in f]
def main():
	data_set = read_MCL("all_prot.end")
	saveData("pan_genome.csv",data_set)

def read_MCL(mcl_file):
	data_set = []	
	f = open(mcl_file,'r')
	for line in f:
		data = ['' for x in range(len(label)+3)]  #菌株数+3
		line= line.strip()
		line_ls = line.split('\t')
		family_info =line_ls[0]
		data[0] = family_info.split(' ')[0] #group_name
		data[1] = re.findall(re.compile(r'(\d*) genes'),family_info)[0]#gene_num
		data[2] = re.findall(re.compile(r'(\d*) taxa'),family_info)[0]#tax_num

		gene_ls = line_ls[1].strip()
		gene_ls = gene_ls.split(' ')
		for s in gene_ls:
			strain = re.findall(r_strain,s)[0][1:-1]
			strain_index = label.index(strain)+3
			if data[strain_index] =='':
				data[strain_index] = re.sub(r_strain,'',s)
			else:
				data[strain_index] = data[strain_index]+';'+re.sub(r_strain,'',s)
		data_set.append(data)
	return data_set
def saveData(savePath,data_set):
	with open(savePath,'w',newline='') as out:
		out_csv = csv.writer(out)
		out_csv.writerows(data_set)
if __name__=="__main__":
    main()
