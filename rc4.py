def RC4(key):
	global S,j
	S = []
	for i in range(256):
		S.append(i)
	j = 0
	for i in range(256):
		j = (j + S[i] + key[i % len(key)]) % 256
		S[i] , S[j] = S[j] , S[i]
	i = j = 0
	i = (i + 1) % 256
	j = (j + S[i]) % 256
	S[i] , S[j] = S[j] , S[i]
	return(S( (S[i] + S[j]) % 256 ))
	
