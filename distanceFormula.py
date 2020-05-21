import math

print("please enter two points co-ordinates ")
x= int(input("type input for 1st point x:"))
y= int(input("type input for 1st point y:"))
z= int(input("type input for 2nd point x:"))

w= int(input("type input for 2nd point y:"))

def distance(a,b,c,d):
	dist=math.sqrt(math.pow((c-a),2)+math.pow((d-b),2))
	return dist

dis=distance(x,y,z,w)
print("i am printing the distance between point (0,0) and (1,1)")
print ("--------------------------------------------------------")
print(dis)

