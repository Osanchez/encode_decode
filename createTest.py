with open('files/test.dat', 'wb') as f:
    f.write(b'\xff' * 3) # you can "multiply" ('*') sequence objects to make repetitions of them
                         # b'\xff' * 3 is shorthand for b'\xff\xff\xff'
    f.write(b'OOOO')
    f.write(b'\xff')
    f.write(b'P' * 8)
    f.write(b'\xff' * 3)
    f.write(b'QQQQ')