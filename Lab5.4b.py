


def rectangle(length,width):
    area=length*width;
    return area

def triangle(length,width):
    area=1/2*length*width;
    return area;

i=0;
while i<2:

    width=float(input("\nEnter  width: "))
    length=float(input("Enter length : "))

    ar=rectangle(length,width);
    at=triangle(length,width);
    print("\nRectangle area : {} ".format(ar))
    print("Triangle area : {} ".format(at))