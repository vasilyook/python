import math
def area_of_circle(a):
    the_res = math.pi *a*a
    print('Площадь круга с радиусом', a)
    print_the_res(the_res)
def area_of_square(a):
    the_res = a*a
    print('Площадь квадрата со стороной', a)
    print_the_res(the_res)
def area_of_rectangle(a,b):
    the_res = a*b
    print('Площадь прямоугольника со сторонами', a, b)
    print_the_res(the_res)
def area_of_romb (a,b):
    the_res = a*b/2
    print('Площадь ромба с диагоналями', a, b)
    print_the_res(the_res)
def area_of_triangle(a,b,c):
    if ((a+b)<=c)or((b+c)<=a)or((a+c)<=b):
        print('Треугольника с такими сторонами не существует!')
    else:
        p=(a+b+c)/2
        the_res = math.sqrt(p*(p-a)*(p-b)*(p-c))
        print('Площадь треугольника со сторонами', a, b, c)
        print_the_res(the_res)
def area_of_trianle_with_angle(a,b,c):
    the_res = math.sin(c*math.pi/180)*a*b/2
    print('Площадь треугольника со сторонами ', a, b)
    print('и углом', c)
    print_the_res(the_res)
def print_the_res(the_res):
    print("равна: ", (round(the_res, 3)))
def main():
    print("Введите, пожалуйста, от одного до трех значений,")
    print("если вы знаете только одно, то введите через пробелы еще 2 нуля")
    print("А мы попробуем посчитать площадь фигуры по вашим значениям!!")
    print('Если вы знаете угол, то введите его последней величиной.')
    try:
        a, b, c = map(float,input('Ваши значения: ').split())
    except:
        print("Пожалуйста, введите числовые значения:")
        a, b, c = map(float,input('Ваши значения: ').split())
    if (a<0) or (b<0) or (c<0):
        print("Очень смешно! Длина - это положительная величина!!!")

    elif (a>0)and (b>0)and(c>0):
        print("Если последнее значение угол, то напишите 'да'")
        print("иначе напишите 'нет'")
        answer = input()

        if (answer == 'да'):
            area_of_trianle_with_angle(a,b,c)

        else:
            area_of_triangle(a,b,c)

    elif (a>0) and (b==0) and (c==0):
        print("Площадь какой фигуры хотите узнать:")
        print("квадрат или круг? ")
        answer = input()
        if (answer == 'квадрат'):
            area_of_square(a)
        elif (answer == 'круг'):
            area_of_circle(a)
        else:
            print('Ну хорошо, раз Вы не определились')
            area_of_square(a)
            area_of_circle(a)
    else:
        area_of_rectangle(a,b)
        print("Либо площадь ромба")
        area_of_romb(a,b)
        
main()
input()
        
        
    
    
    
    
