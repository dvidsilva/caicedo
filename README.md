# Caicedo

Andrés Caicedo nació en Cali, Valle, en 1951 y, a pesar de su prematura muerte
(1977), descolló en el campo literario colombiano. Escribió numerosos cuentos,
recopilados en varios volúmenes: El atravesado (relato, 1975), Angelitos
empantanados o historia para jovencitos (1977), y Berenice (1978). Su única
novela ¡Qué viva la música! ha tenido gran difusión entre el público.

Con este proyecto buscamos hacer una forma de necromancia que lo trae de vuelta
a nuestras vidas de forma cibernetica.

## Getting started

### Requirements

[Installation docs](./docs/install.md)

### Input file

Generate input file from txt source:

macbook:
```
cat txt/*.txt >> input/input.txt
```

Generate clean input:

```
python clean.py >> input/input_clean.txt
```

## Acknowledgements

Thanks to Karpathy for an amazing explanation and the source code for this model.

Honestly wouldn't have attempted this if he hadn't made it so easy. Cheers to
open source and community.

[Repo](https://github.com/karpathy/ng-video-lecture/blob/master/bigram.py)

[Youtube lecture](https://www.youtube.com/watch?v=kCc8FmEb1nY)

## LICENSE

[The Satire License (TSL)](./LICENSE)

## Author

[@dvidsilva](https://dvidsilva.com)

## Original README:

nanogpt-lecture

Code created in the Neural Networks: Zero To Hero video lecture series,
specifically on the first lecture on nanoGPT. Publishing here as a Github repo
so people can easily hack it, walk through the git log history of it, etc.

NOTE: sadly I did not go too much into model initialization in the video
lecture, but it is quite important for good performance. The current code will
train and work fine, but its convergence is slower because it starts off in a
not great spot in the weight space. Please see nanoGPT
[model.py](https://github.com/karpathy/nanoGPT/blob/master/model.py)
for # init all
weights comment, and especially how it calls the _init_weights function. Even
more sadly, the code in this repo is a bit different in how it names and stores
the various modules, so it's not possible to directly copy paste this code here.
My current plan is to publish a supplementary video lecture and cover these
parts, then I will also push the exact code changes to this repo. For now I'm
keeping it as is so it is almost exactly what we actually covered in the video.

