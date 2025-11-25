def to_i(e):
  return int(e)

l = map(to_i, raw_input().rstrip().split(" "))
l.sort()
l.reverse()

print "{} {} {} {} {}".format(l[0], l[1], l[2], l[3], l[4])