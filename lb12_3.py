import def_for_lb12_3

cube_side = float(input("Введіть довжину сторони куба: "))

if cube_side > 0:
    print("Об'єм куба:", def_for_lb12_3.volume(cube_side))
    print("Площа бічної поверхні куба:", def_for_lb12_3.surface_area(cube_side))
    