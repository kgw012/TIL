str = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

point_list = list(map(lambda c: ord('E') - ord(c), str))
print(sum(point_list))