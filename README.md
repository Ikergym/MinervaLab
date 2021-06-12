# MinervaLab 2.0 Bertsioaren biltegia

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Ikergym/MinervaLab/master)
[![Documentation Status](https://readthedocs.org/projects/minervalab/badge/?version=latest)](https://minervalab-v20.readthedocs.io/en/latest/)

----------------------------

MinervaLab "Termodinamika eta Fisika Estatistikoa" irakasgaiaren irakaskuntza-prozesuan laguntzeko euskarri digitala da. Zehatzago, aplikazio-sorta bat da, irakasgaian zehar agertzen diren adierazpide grafikoak modu interaktiboan irudikatzen dituena, besteak beste. Proiektuaren lehen bertsioa 2020ko ekainean argitaratu zuen Jon Gabirondo López-ek bere Fisikako Graduko GrALean.

Jatorrizko proiektuaren bitlegia [hemen](https://github.com/jongablop/MinervaLab) topa daiteke:



<br/>

## Exekutatu sarean

Notebook-ak nabigatzailean exekutatu daitezke [Binder](https://mybinder.org/) erabiliz, aplikazio bakoitzaren helbidean klikatuta.


<br/>

## 2.0 Bertsioko aplikazio berriak:

Aplikazioei erreferentzia egiteko, zenbakizko kode bat esleitu zaio aplikazio bakoitzari, lehenengo bertsioko numerazio-sistemari jarraituz. Tabla honetan bigarren bertsiorako garatutako aplikazioen zerrenda aurki daiteke. Aplikazioaren helbidean klikatuz gero, Binderreko notebook exekutagarria irekiko da. Iturri-kodea ikusteko biltegi honetan bertan ireki daitezke aplikazioak, dagokien helbidean

<center>
<table >
    <thead>
        <tr>
            <th>Kodea #</th>
            <th>Kontzeptua</th>
            <th>Helbidea</th>
            <th>Deskribapena</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>#121-000</td>
            <td>Bolumen konstanteko gas termometroa eta zero printzipioa</td>
            <td><a href='https://mybinder.org/v2/gh/Ikergym/MinervaLab/master?filepath=apps%2Fideal_gas%2Fgas_thermometer.ipynb'>apps/ideal_gas/gas_thermometer.ipynb</a></td>
            <td>Gas ezberdinentzako tenperatura enpirikoaren neurketak presio ezberdinetarako.</td>
        </tr>
        <tr>
            <td>#122-000</td>
            <td>Prozesu kuasiestatiko sinpleak</td>
            <td><a href='https://mybinder.org/v2/gh/Ikergym/MinervaLab/master?filepath=apps%2Fideal_gas%2Fsimple_processes.ipynb'>apps/ideal_gas/simple_processes.ipynb</a></td>
            <td>Gas idealaren kasurako prozesu isokoro, isobaro, isotermo eta adiabatikoen azterketa.</td>
        </tr>
        <tr>
            <td>#123-000</td>
            <td>Prozesu politropikoak</td>
            <td><a href='https://mybinder.org/v2/gh/Ikergym/MinervaLab/master?filepath=apps%2Fideal_gas%2Fpolytropic_processes.ipynb'>apps/ideal_gas/polytropic_processes.ipynb</a></td>
            <td>Gas idealaren kasurako, indize ezberdineko prozesu politropikoen azterketa.</td>
        </tr>
        <tr>
            <td>#124-000</td>
            <td>Ziklo termodinamikoak eta motore termikoak</td>
            <td><a href='https://mybinder.org/v2/gh/Ikergym/MinervaLab/master?filepath=apps%2Fideal_gas%2Fthermodynamic_cycles.ipynb'>apps/ideal_gas/thermodynamic_cycles.ipynb</a></td>
            <td>Carnot, Diesel eta Stirling zikloen azterketa.</td>
        </tr>
        <tr>
            <td>#131-000</td>
            <td>Banaketa estatistikoak</td>
            <td><a href='https://mybinder.org/v2/gh/Ikergym/MinervaLab/master?filepath=apps%2Ffermi_gas%2Fdistribution_comparison.ipynb'>apps/fermi_gas/distribution_comparison.ipynb</a></td>
            <td>Fermi-Dirac, Bose-Einstein eta Maxwell-Boltzmann banaketa-funtzioen arteko konparazioa.</td>
        </tr>
        <tr>
            <td>#132-000</td>
            <td>Fermi-Dirac banaketa eta potentzial kimikoa</td>
            <td><a href='https://mybinder.org/v2/gh/Ikergym/MinervaLab/master?filepath=apps%2Ffermi_gas%2Fchemical_potential.ipynb'>apps/fermi_gas/chemical_potential.ipynb</a></td>
            <td>Fermi-Dirac banaketaren bidez potentzial kimikoaren esangura ulertzeko aplikazioa.</td>
        </tr>
        <tr>
            <td>#133-000</td>
            <td>Fermi-Dirac banaketa eta egoera dentsitatea</td>
            <td><a href='https://mybinder.org/v2/gh/Ikergym/MinervaLab/master?filepath=apps%2Ffermi_gas%2Fdensity_of_states.ipynb'>apps/fermi_gas/density_of_states.ipynb</a></td>
            <td>Egoera-dentsitatearen eragina ulertzeko aplikazioa, Fermi-Dirac banaketaren baitan.</td>
        </tr>
        <tr>
            <td>#134-000</td>
            <td>Bero ahalmen elektronikoa metaletan</td>
            <td><a href='https://mybinder.org/v2/gh/Ikergym/MinervaLab/master?filepath=apps%2Ffermi_gas%2Fspecific_heat.ipynb'>apps/fermi_gas/specific_heat.ipynb</a></td>
            <td>Fermi-Dirac banaketa erabiliz, metalen tenperatura baxuko bero-ahalmena kalkulatzeko tresna.</td>
        </tr>
    </tbody>
</table>
</center>

<br/>

## Dependentziak:
+ `bqplot` (version = 0.11.6)
+ `ipywidgets`
+ `scipy`
+ `numpy`
+ `pip`
+ `matplotlib`
+ `qgrid`
+ `ipyvolume`
+ `pandas`
+ `appmode`

<br/>

## Nola instalatu

### Pip erabiliz:

1. Instalatu `virtualenv` eta sortu ingurune birtual berri bat MinervaLab-en instalazioa isolatzeko: [virtualenv installation guide](https://virtualenv.pypa.io/en/latest/installation.html).

2. [Aktibatu ingurune birtuala](https://virtualenv.pypa.io/en/latest/user_guide.html) eta Jupyter instalatu: [install Jupyter using pip](https://jupyter.readthedocs.io/en/latest/install.html#alternative-for-experienced-python-users-installing-jupyter-with-pip).

3. Instalatu aipatutako dependentzia guztiak.

4. Biltegia klonatu (erabili `git clone https://github.com/jongablop/MinervaLab.git`) edo biltegia deskargatu bestela.

5. Ingurunearen `root` karpetan jarri eta exekutatu Jupyter:
```
    cd MinervaLab
    jupyter notebook
```

<br/>

## Lizentzia

Software hau GNU General Public License v3.0. lizentziapean argitaratuta dago. Informazio gehiagorako ikus [LIZENTZIA](LICENSE.md).

<br/>
