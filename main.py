from tempfile import TemporaryFile

with TemporaryFile(mode='w+t') as f:
    f.write('Hello, world!')
    f.seek(0)
    print(f.read())
