# #122-000 Simpe Processes

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Ikergym/MinervaLab/b561bc2db367159819e9518d9466bdbc39e58a7e?filepath=apps%2Fideal_gas%2FSimple%20Processes.ipynb)

## Deskribapena
Aplikazio honen helburua gas idealetan lau prozesu arruntenak aztertzea da: isokoroa, isobaroa, isotermoa eta adiabatikoa. Horretarako, hasierako puntu batetik abiatuz, lau prozesuak irudikatuko dira $pV$ diagrama batean. Prozesu bakoitzak mugatzen duen kurba erakusteaz gain, bakoitzari dagokion lana beroa eta energia aldaketa ere kalkulatuko dira.

## Aplikazioaren erabilera
Lehenik, gas mota finkatu behar da (monoatomikoa edo diatomikoa) dropdown menu baten bidez. Ondoren mol kopurua finkatu behar da slider bat erabiliz. Behin gasa zehaztuta, hasierako puntuaren bolumena ($V_i$) eta presioa ($p_i$) finkatzeko slider bana erabili behar dira. Hasierako parametro hauek definituta, hasierako puntuaren tenperatura finkatuta geratzen da, gas idealaren oreka-ekuazio mekanikoa dela eta:

$$ pV = NRT $$

Grafikan lau prozesuak grafikatuko dira kolore ezberdinez. Horietako bat aukeratzeko beste dropdown menu bat erabili behar da. Aukeratutako prozesuaren lerroa opakoa egingo da eta beste hiruak gardenagoak izango dira. Grafikaren azpian amaierako egoera aukeratzeko kontrolak daude:

 - Prozesua isokoroa bada: bukaerako bolumena finkatuta dago hasierako bolumenaren berdina izan behar delako, beraz, $V_f$-ri dagokion sliderra blokeatuta egongo da. Kasu horretan bukaerako presioa zehazteko slider bat agertuko da (hau zehaztean bukaerako tenperatura ere zehaztuta geratuko da oreka-ekuazioarengatik).

 - Prozesua isokoroa ez bada: bukaerako bolumena zehazteko sliderra desblokeatuko da. Bukerako presioa eta tenperatura zehaztuta geratuko dira egoera-ekuazioa eta prozesuari dagokion ekuazioarengatik.

 Eskubian prozesuan zehar egindako lana, trukatutako beroa eta sistemaren energia aldaketa erakusten dira. Espero bezala:

  - Prozesu isokoroetan lana nulua da
  - Prozesu isotermoetan energiaren aldaketa nulua da
  - Prozesu adiabatikoetan trukatutako beroa nulua da (hau ez da guztiz egia izango, integrazio numerikoa egiteko erabitlzen den zehaztasunaren araberakoa baita, baina dena den, energia aldaketa baino magnitude orden batzuk baxuagoa izango da)
