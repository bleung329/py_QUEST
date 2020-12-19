syms lambda
K = sym('K',[4 4]);
K = K-lambda*eye(4)
det(K)
diff(det(K),lambda)
simplify(det(K)/diff(det(K),lambda))