# Table of Contents

 1. [Comprehensions](#Comprehensions)

---

# Comprehensions

In [comprehensions.py](comprehensions.py), I present some examples of comprehensions and their
counterparts in the for-loop format.

## Results
I noticed some differences when running this file with different python versions. See the runs below. Note that these were run on a Macbook running using an M1 ARM chip. Also keep in mind that python3.7 was tested while being run through the Rosetta Stone built-in software.

### Python 3.7 'i386'
```
useless-utils/python $ python3.7 comprehensions.py
               simple_comprehension : 1.1686716079711914e-05 seconds
                        simple_loop : 1.2896616458892822e-05 seconds

               double_comprehension : 1.000502109527588e-06 seconds
                        double_loop : 1.5258383750915527e-06 seconds

               triple_comprehension : 1.745781898498535e-06 seconds
                        triple_loop : 2.8176331520080565e-06 seconds
```

### Python 3.8 'arm'
```
useless-utils/python $ python3.8 comprehensions.py
               simple_comprehension : 7.931907176971436e-06 seconds
                        simple_loop : 8.383991718292237e-06 seconds

               double_comprehension : 5.942320823669433e-07 seconds
                        double_loop : 9.423208236694335e-07 seconds

               triple_comprehension : 9.896135330200195e-07 seconds
                        triple_loop : 1.6242051124572754e-06 seconds
```

### Python 3.9 'arm'
```
useless-utils/python $ python3.9 comprehensions.py
               simple_comprehension : 7.163276672363281e-06 seconds
                        simple_loop : 8.049142360687256e-06 seconds

               double_comprehension : 5.929708480834961e-07 seconds
                        double_loop : 9.275674819946289e-07 seconds

               triple_comprehension : 9.762144088745118e-07 seconds
                        triple_loop : 1.5753746032714843e-06 seconds
```

### Python 3.10 'arm'
```
useless-utils/python $ python3.10 comprehensions.py
               simple_comprehension : 7.16789722442627e-06 seconds
                        simple_loop : 7.846167087554932e-06 seconds

               double_comprehension : 5.494737625122071e-07 seconds
                        double_loop : 8.847880363464355e-07 seconds

               triple_comprehension : 9.064674377441406e-07 seconds
                        triple_loop : 1.478886604309082e-06 seconds
```

### Python 3.11 'arm'
```
useless-utils/python $ python3.11 comprehensions.py
               simple_comprehension : 5.7663965225219725e-06 seconds
                        simple_loop : 5.733625888824463e-06 seconds

               double_comprehension : 4.85377311706543e-07 seconds
                        double_loop : 4.906034469604492e-07 seconds

               triple_comprehension : 8.670639991760254e-07 seconds
                        triple_loop : 9.360575675964355e-07 seconds
```

There are a couple of surprising observations I made when observing these results.
 1. For one, when it comes to the `simple` tests (labeled as `simple_comprehension` and `simple_loop`), of the different python versions, all except `python3.11` showed faster times with the list comprehension over the for-loop, whereas `python3.11` showed faster times with the for-loop than the list comprehension. While `python3.11` is the fastest of all the prior python versions mentioned here, it is clear that the recent upgrades to python 3 made the difference in execution time between the `simple_comprehension` test and `simple_loop` test negligible.
 2. As we move towards the `double` and `triple` tests, it is clear that the list comprehension method is much faster, boasting a
    * `37.9%` speed boost for `python3.7`'s `triple` tests,
    * `38.9%` for `python3.8`,
    * `38.0%` for `python3.9`,
    * `38.5%` for `python3.10`,
    * `7.37%` for `python3.11`. \
    
 * => Between all the python versions tested, `python3.11`'s data is the outlier.All the other python versions show a great difference in performance between using the nested for loops and the list comprehension, but it appears that newer versions of python 3 will not reveal such a drastic difference in performance.
