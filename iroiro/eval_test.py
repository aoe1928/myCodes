a = compile('for x in range(1):\n import time\n time.sleep(2)', '', 'single')

for _ in range(3):
    exec(a)