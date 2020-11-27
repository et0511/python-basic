# test for Add
try:
    from Add import Add
    from multiply import Multiply
except ImportError as e:
    print(e)

a = Add()
out = a.forward(10, 20)
print(out)
print(a)


# test for Multoply
m = Multiply()
out = m.forward(10, 20)
print(out)      # 200
print(m)        # 'multiply (x=10, y=20)'

