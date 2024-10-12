# Cautions against using

## human-like movements and scroll

Do not try using 

```bash
from selenium.webdriver.common.action_chains import ActionChains
```

or "human like mouse movements" or "human like scroll". 

It causes this sort of error and immediate exit:

```bash
Navigating to https://forvo.com/languages-pronunciations/ga/page-128/
Unexpected error occurred: Message: move target out of bounds
(Session info: chrome=129.0.6668.100)
Stacktrace:
0   chromedriver                        0x000000010de09d08 chromedriver + 4996360
1   chromedriver                        0x000000010de015ca chromedriver + 4961738
2   chromedriver                        0x000000010d9a4b5d chromedriver + 387933
3   chromedriver                        0x000000010da3c55d chromedriver + 1008989
4   chromedriver                        0x000000010da159b2 chromedriver + 850354
5   chromedriver                        0x000000010da33a00 chromedriver + 973312
6   chromedriver                        0x000000010da15753 chromedriver + 849747
7   chromedriver                        0x000000010d9e4635 chromedriver + 648757
8   chromedriver                        0x000000010d9e4e5e chromedriver + 650846
9   chromedriver                        0x000000010ddcfff0 chromedriver + 4759536
10  chromedriver                        0x000000010ddd4f08 chromedriver + 4779784
11  chromedriver                        0x000000010ddd55d5 chromedriver + 4781525
12  chromedriver                        0x000000010ddb2a99 chromedriver + 4639385
13  chromedriver                        0x000000010ddd58c9 chromedriver + 4782281
14  chromedriver                        0x000000010dda4034 chromedriver + 4579380
15  chromedriver                        0x000000010ddf19f8 chromedriver + 4897272
16  chromedriver                        0x000000010ddf1bf3 chromedriver + 4897779
17  chromedriver                        0x000000010de011ce chromedriver + 4960718
18  libsystem_pthread.dylib             0x00007ff80338c18b _pthread_start + 99
19  libsystem_pthread.dylib             0x00007ff803387ae3 thread_start + 15

WebDriver has been quit successfully
```