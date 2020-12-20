%Written by Brian Leung

%PURPOSE:
%This file is just a mish mash of things that helped me work out what the
%characteristic equation was, specifically for the work done in eig_helper.
%This is more scrap paper than actual code, so feel free to ignore whatever is in this file.

syms L K K1_1 K1_2 K1_3 K1_4 K2_1 K2_2 K2_3 K2_4 K3_1 K3_2 K3_3 K3_4 K4_1 K4_2 K4_3 K4_4
clc;
K = sym('K',[4 4]);
K = K-L*eye(4);
simplify(det(K))

K1_1=4;K1_2=1;K1_3=3;K1_4=4;K2_1=5;K2_2=6;K2_3=7;K2_4=8;K3_1=9;K3_2=10;K3_3=11;K3_4=12;K4_1=13;K4_2=14;K4_3=15;K4_4=13;
L=1;

subs(simplify(det(K)))
diff(det(K),L);
simplify(det(K)/diff(det(K),L))
l3_coeff = - K2_2*L^3 - K3_3*L^3 - K4_4*L^3 - K1_1*L^3;

l2_coeff = (K1_1*K2_2 - K1_2*K2_1 + K1_1*K3_3 - K1_3*K3_1 + K1_1*K4_4 - K1_4*K4_1 + K2_2*K3_3 - K2_3*K3_2 + K2_2*K4_4 - K2_4*K4_2 + K3_3*K4_4 - K3_4*K4_3); 
l1_coeff = -K1_1*K2_2*K3_3*L + K1_1*K2_3*K3_2*L + K1_2*K2_1*K3_3*L - K1_2*K2_3*K3_1*L - K1_3*K2_1*K3_2*L + K1_3*K2_2*K3_1*L - K1_1*K2_2*K4_4*L + K1_1*K2_4*K4_2*L + K1_2*K2_1*K4_4*L - K1_2*K2_4*K4_1*L - K1_4*K2_1*K4_2*L + K1_4*K2_2*K4_1*L - K1_1*K3_3*K4_4*L + K1_1*K3_4*K4_3*L + K1_3*K3_1*K4_4*L - K1_3*K3_4*K4_1*L - K1_4*K3_1*K4_3*L + K1_4*K3_3*K4_1*L - K2_2*K3_3*K4_4*L + K2_2*K3_4*K4_3*L + K2_3*K3_2*K4_4*L - K2_3*K3_4*K4_2*L - K2_4*K3_2*K4_3*L + K2_4*K3_3*K4_2*L;
l0_coeff = K1_1*K2_2*K3_3*K4_4 - K1_1*K2_2*K3_4*K4_3 - K1_1*K2_3*K3_2*K4_4 + K1_1*K2_3*K3_4*K4_2 + K1_1*K2_4*K3_2*K4_3 - K1_1*K2_4*K3_3*K4_2 - K1_2*K2_1*K3_3*K4_4 + K1_2*K2_1*K3_4*K4_3 + K1_2*K2_3*K3_1*K4_4 - K1_2*K2_3*K3_4*K4_1 - K1_2*K2_4*K3_1*K4_3 + K1_2*K2_4*K3_3*K4_1 + K1_3*K2_1*K3_2*K4_4 - K1_3*K2_1*K3_4*K4_2 - K1_3*K2_2*K3_1*K4_4 + K1_3*K2_2*K3_4*K4_1 + K1_3*K2_4*K3_1*K4_2 - K1_3*K2_4*K3_2*K4_1 - K1_4*K2_1*K3_2*K4_3 + K1_4*K2_1*K3_3*K4_2 + K1_4*K2_2*K3_1*K4_3 - K1_4*K2_2*K3_3*K4_1 - K1_4*K2_3*K3_1*K4_2 + K1_4*K2_3*K3_2*K4_1;
l1_coeff_simpl = L*(- K1_1*K2_2*K3_3 + K1_1*K2_3*K3_2 + K1_2*K2_1*K3_3 - K1_2*K2_3*K3_1 - K1_3*K2_1*K3_2 + K1_3*K2_2*K3_1 - K1_1*K2_2*K4_4 + K1_1*K2_4*K4_2 + K1_2*K2_1*K4_4 - K1_2*K2_4*K4_1 - K1_4*K2_1*K4_2 + K1_4*K2_2*K4_1 - K1_1*K3_3*K4_4 + K1_1*K3_4*K4_3 + K1_3*K3_1*K4_4 - K1_3*K3_4*K4_1 - K1_4*K3_1*K4_3 + K1_4*K3_3*K4_1 - K2_2*K3_3*K4_4 + K2_2*K3_4*K4_3 + K2_3*K3_2*K4_4 - K2_3*K3_4*K4_2 - K2_4*K3_2*K4_3 + K2_4*K3_3*K4_2);
l1_coeff_only = K1_1*(-K2_2*K3_3 + K2_3*K3_2 - K2_2*K4_4 + K2_4*K4_2 - K3_3*K4_4 + K3_4*K4_3) + K1_2*(K2_1*K3_3 - K2_3*K3_1+ K2_1*K4_4 - K2_4*K4_1) + K1_3*(-K2_1*K3_2 + K2_2*K3_1  + K3_1*K4_4 - K3_4*K4_1)  + K1_4*(-K2_1*K4_2 + K2_2*K4_1  - K3_1*K4_3 + K3_3*K4_1) + K2_2*(-K3_3*K4_4 + K3_4*K4_3) + K2_3*(K3_2*K4_4 - K3_4*K4_2) + K2_4*(-K3_2*K4_3 + K3_3*K4_2);
subs(l0_coeff)
subs(l1_coeff)
subs(l2_coeff)
subs(l3_coeff)
subs(L^4+l3_coeff*L^3+l2_coeff*L^2+l1_coeff*L+l0_coeff)
subs(diff(det(K),L))