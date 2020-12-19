#PURPOSE:
#The name is a lot fancier than it actually is.
#This is just a short script used to convert the symbolic notation of Matlab (from the work done in 
#determinant_helper.m) into numpy/python notation. Nothing particularly significant, I'm just lazy.

num_string='K1_1*K2_2*K3_3*K4_4 - K1_1*K2_2*K3_4*K4_3 - K1_1*K2_3*K3_2*K4_4 + K1_1*K2_3*K3_4*K4_2 + K1_1*K2_4*K3_2*K4_3 - K1_1*K2_4*K3_3*K4_2 - K1_2*K2_1*K3_3*K4_4 + K1_2*K2_1*K3_4*K4_3 + K1_2*K2_3*K3_1*K4_4 - K1_2*K2_3*K3_4*K4_1 - K1_2*K2_4*K3_1*K4_3 + K1_2*K2_4*K3_3*K4_1 + K1_3*K2_1*K3_2*K4_4 - K1_3*K2_1*K3_4*K4_2 - K1_3*K2_2*K3_1*K4_4 + K1_3*K2_2*K3_4*K4_1 + K1_3*K2_4*K3_1*K4_2 - K1_3*K2_4*K3_2*K4_1 - K1_4*K2_1*K3_2*K4_3 + K1_4*K2_1*K3_3*K4_2 + K1_4*K2_2*K3_1*K4_3 - K1_4*K2_2*K3_3*K4_1 - K1_4*K2_3*K3_1*K4_2 + K1_4*K2_3*K3_2*K4_1'
while(num_string.count('_')!=0):
	loc = num_string.find('_')
	right = str(int(num_string[loc+1])-1)
	left = str(int(num_string[loc-1])-1)
	num_string = num_string.replace(num_string[loc-1]+'_'+num_string[loc+1],'['+left+','+right+']')
	print(loc)
print(num_string)