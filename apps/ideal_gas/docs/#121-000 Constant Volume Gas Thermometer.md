# #121-000 Constant Volume Gas Thermometer

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Ikergym/MinervaLab/7da11ec6d08014af702ea7892b24ffdc6896ba85?filepath=apps%2Fideal_gas%2FConstant%20Volume%20Gas%20Thermometer.ipynb)



## Deskribapena
Programa honen helburua gas idealaren tenperatura nola eraikitzen den adieraztea da. Horretarako gas ezberdinetarako eta hauen $p_{pt}$ balio ezberdinetarako tenperatura enpirikoaren balio ezberdinak grafikatuko dira. Bestalde $p_{pt} \rightarrow 0$ limitean gas guztiek balio berera konbergitzen dutela ikusko da. Balio hau da, hain zuzen ere, gas idealaren tenperatura.

## Aplikazioaren erabilpena
Lehenik neurtu nahi den tenperatura hautatu behar da (gas idealaren eskalan). Horretarako, lehenengo slider-a erabili behar da. Ondoren, gasa aukeratu behar da dropdown menu baten bidez. Hiru gas daude erabilgarri: $H_2$, $He$ eta $N_2$. Hurrengo sliderraren bidez $p_{pt}$-ren balioa aukeratu daiteke (hau da, gasak izango duen presioa, uraren puntu hirukoitzarekin oreka termikoan dagoenean).

Eskubiko irudian puntu bat azaltzen da $\Theta$ vs $p_{pt}$ grafikoan. $p_{pt}$ mugituz puntua mugituko da. $\Theta$-ren aldiuneko balio zehatza sliderraren azpian azalduko da (puntuaren gainean hover eginez ere $x$,$y$ koordenatuak ikus daitezke).

Puntuak finkatu daitezke grafikoan "gorde puntua" botoia sakatuz. Modu honetan hainbat $p_{pt}$-rentzat $\Theta$-k lortzen dira. Puntu hauek lerro zuzen bat osatzen dute gas bakoitzarentzat. Puntu guzti hauek ezabatzeko "ezabatu puntuak" botoia erabili daiteke.

Azkenik, puntu guztiak lotzen dituzten lerroak (gas bakoitzarentzat lerro bat) erakutsi/ezkutatu daitezke "erakutsi lerroak" checkbox-a aktibatuz/desaktibatuz.

Tenperaturaren sliderra aldatuz, tenperatura ezberdinetarako errepikatu daiteke prozesua. Espero bezala, $T=273.16K$ aukeratuz gero, hiru gasentzako $\Theta$ berdina izango da $p_{pt}$ guztientzako (egoera termiko horren tenperatura finkoa delako hitzarmenez).
