# #123-000 Polytropic Processes

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Ikergym/MinervaLab/AplikazioBerriak?filepath=apps%2Fideal_gas%2FPolytropic%20Processes.ipynb)

## Deskribapena
Aplikazio honen helburua gas idealetan prozesu politropikoak aztertzea da. Horretarako, hasierako puntu batetik abiatuz, $j $ indize ezberdineko zenbait prozesu irudikatuko dira $pV$ diagrama batean. Prozesu bakoitzak mugatzen duen kurba erakusteaz gain, bakoitzari dagokion lana beroa eta energia aldaketa ere kalkulatuko dira.

## Aplikazioaren erabilera
Hasteko, marraztuko diren kurbak definitu behar dira. Horretarako, hiru slider daude goiko aldean, $j$ minimoa, $j$ maximoa eta kurba kopurua finkatzeko. Kurbak sortzeko "sortu kurbak" botoia sakatu behar da.

Ezkerrean, gasaren kontrolak daude. Gas mota finkatu behar da (monoatomikoa edo diatomikoa) dropdown menu baten bidez. Mol kopurua finkatu behar da slider bat erabiliz. Behin gasa zehaztuta, hasierako puntuaren bolumena ($V_i$) eta presioa ($p_i$) finkatzeko slider bana erabili behar dira. Hasierako parametro hauek definituta, hasierako puntuaren tenperatura finkatuta geratzen da, gas idealaren oreka-ekuazio mekanikoa dela eta:

$$ pV = NRT $$

Grafikan prozesu guztiak irudikatuko dira kolore ezberdinez. Horietako bat aukeratzeko grafikaren ezkerran dagoen sliderra erabili behar da. Aukeratutako prozesuaren lerroa opakoa egingo da eta gainontzekoak gardenagoak izango dira. Grafikaren azpian amaierako egoeraren bolumena aukeratzeko sliderra dago. Honek amaierako presioa eta tenperatura finkatuko ditu oreka-ekuazioa eta prozesuaren ekuazioarengatik.

 Eskubian prozesuan zehar egindako lana, trukatutako beroa eta sistemaren energia aldaketa erakusten dira. "Lana erakutsi" gelaxka markatuz gero, $pdV$-ren integrala irudikatuko da grafikaren azpiko azalera erakutsiz.

  - Prozesu isotermoetan($j=0$) energiaren aldaketa nulua da
  - Prozesu adiabatikoetan ($j=\gamma$) trukatutako beroa nulua da (hau ez da guztiz egia izango, integrazio numerikoa egiteko erabitlzen den zehaztasunaren araberakoa baita, baina dena den, energia aldaketa baino magnitude orden batzuk baxuagoa izango da)
  - Prozesu adiabatikoen $j$ gas motaren araberakoa da ($j=5/3$ monoatomikoa bada eta $j=7/5$ diatomikoa bada)
