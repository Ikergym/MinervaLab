<p align="center">
  <img width="90%" src="https://github.com/jongablop/MinervaLab/blob/master/static/images/logo.png">
</p>
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jongablop/MinervaLab/master)
[![Documentation Status](https://readthedocs.org/projects/minervalab/badge/?version=latest)](https://minervalab.readthedocs.io/en/latest/?badge=latest)
----------------------------

MinervaLab is a collection of interactive simulations of Thermodynamics and Statistical Physics developed in order to provide both teachers and students with a tool to visualize some specially difficult concepts related to this subjects.

<br/>

## Try it now live:

Notebooks can be executed directly on [Binder](https://mybinder.org/) just by click on the file paths of the table below.

<br/>

## Structure:

A Product Breakdown Structure (PBS) system has been used during the development of this proyect, assigning a unique code to every concept/program/element. The following chart can be useful as a guide to understand the names of the variables used along all the programs.

<center>
<table >
    <thead>
        <tr>
            <th>PBS #</th>
            <th>Concept</th>
            <th>File path</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td width="20%">#110-000</td>
            <td>Van der Waals equation of state</td>
            <td>apps/van_der_waals</td>
            <td>A collection of programs aimed to visualize the different aspects of the phase transitions of a gas that follows the Van der Waals equation of state.</td>
        </tr>
        <tr>
            <td>#111-000</td>
            <td>Maxwell’s construction on van der Waals isotherms</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fp_v_2D.ipynb'>apps/van_der_waals/p_v_2D.ipynb</a></td>
            <td>A two-dimensional representation of the p(v,T) space during a gas-liquid phase transition (using reduced variables).</td>
        </tr>
        <tr>
            <td>#112-000</td>
            <td>Visualization of molar volume during a liquid-gas phase transition</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fphase_transition_volume.ipynb'>apps/van_der_waals/phase_transition_volume.ipynb</a></td>
            <td>A visualization of how each phase volume changes during a phase transition.</td>
        </tr>
        <tr>
            <td>#113-000</td>
            <td>Critical points for various fluids</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fcritical_points.ipynb'>apps/van_der_waals/critical_points.ipynb</a></td>
            <td>An interactive database of Van der Waals equation's a and b parameters that allows to visualize the critical points of a sort of elements.</td>
        </tr>
        <tr>
            <td>#114-000</td>
            <td>Effect of a and b in van der Waals isotherms</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Feffect_of_a_and_b.ipynb'>apps/van_der_waals/effect_of_a_and_b.ipynb</a></td>
            <td>A sort of representations of p(v,T) which gives the opportunity to interact with the a and b parameters in absolute variables.</td>
        </tr>
        <tr>
            <td>#115-000</td>
            <td>Compare elements’ isotherms</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fcompare_elements.ipynb'>apps/van_der_waals/compare_elements.ipynb</a></td>
            <td>A program which allows to compare the p(v,T) isotherms for a given sort of elements.</td>
        </tr>
        <tr>
            <td>#116-000</td>
            <td>Van der Waals isotherms in 3D</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fp_v_T_3D.ipynb'>apps/van_der_waals/p_v_T_3D.ipynb</a></td>
            <td>A three-dimensional representation of the p(v,T) space during a gas-liquid phase transition (using reduced variables).</td>
        </tr>
        <tr>
            <td>#117-000</td>
            <td>Chemical potential of a van der Waals real gas</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fchemical_potential.ipynb'>apps/van_der_waals/chemical_potential.ipynb</a></td>
            <td>A program that allows to construct the chemical potential starting from the p(v,T) space.</td>
        </tr>
        <tr>
            <td>#118-000</td>
            <td>Mathematical analysis of the van der Waals isotherms</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fmathematical_analysis.ipynb'>apps/van_der_waals/mathematical_analysis.ipynb</a></td>
            <td>A visualization of Vander Waals' equation of state from a analytical point of view.</td>
        </tr>
        <tr>
            <td>#119-000</td>
            <td>Mathematical analysis of the effect of a and b parameters</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fparameters_analysis.ipynb'>apps/van_der_waals/parameters_analysis.ipynb</a></td>
            <td>A visualization of Vander Waals' equation of state from a analytical point of view in order to study the effect of a and b parameters on the mathematical function.</td>
        </tr>
        <tr>
            <td>#11A-000</td>
            <td>Stability condition on van der Waals isotherms</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fstability.ipynb'>apps/van_der_waals/stability.ipynb</a></td>
            <td>A visualization of dp/dv in order to study the stability of the system.</td>
        </tr>
        <tr>
            <td>#11B-000</td>
            <td>p-T plane and Gibbs free energy</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fp_T_2D.ipynb'>apps/van_der_waals/p_T_2D.ipynb</a></td>
            <td>An interactive visualization of the p(T) plane and the Gibbs free energy for a gas-liquid phase transition.</td>
        </tr>
        <tr>
            <td>#11C-000</td>
            <td>Effect of a and b in van der Waals isotherms (reduced variables)</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Feffect_of_a_and_b_reduced.ipynb'>apps/van_der_waals/effect_of_a_and_b_reduced.ipynb</a></td>
            <td>A sort of representations of p(v,T) which gives the opportunity to interact with the a and b parameters in reduced variables.</td>
        </tr>
        <tr>
            <td>#11D-000</td>
            <td>Change in molar entropy during a first-order phase transition</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fentropy.ipynb'>apps/van_der_waals/entropy.ipynb</a></td>
            <td>The aim of this notebook is to visualize the change in molar entropy during a first-orden liquid-gas transition.</td>
        </tr>
    </tbody>
</table>
</center>

<br/>

## Dependencies:
+ `bqplot` (version = 0.11.6)
+ `ipywidgets`
+ `scipy`
+ `numpy`[[1]](#1)[[2]](#2)
+ `pip`
+ `matplotlib`[[3]](#3)
+ `qgrid`
+ `ipyvolume`
+ `pandas`[[4]](#4)

<br/>

## License

This software is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE.md) file for details.

<br/>

## References


<a id="1">[1]</a>
Travis E. Oliphant.
<strong>A guide to NumPy</strong>,
USA: Trelgol Publishing, (2006).

<a id="2">[2]</a> Stéfan van der Walt, S. Chris Colbert and Gaël Varoquaux.
<strong>The NumPy Array: A Structure for Efficient Numerical Computation</strong>,
Computing in Science &amp; Engineering, <strong>13</strong>, 22-30 (2011),
<a class="reference external" href="http://dx.doi.org/10.1109/MCSE.2011.37">DOI:10.1109/MCSE.2011.37</a> (<a class="reference external" href="http://scitation.aip.org/content/aip/journal/cise/13/2/10.1109/MCSE.2011.37">publisher link</a>)

<a id="3">[3]</a>
 J. D. Hunter, <strong>Matplotlib: A 2D Graphics Environment</strong>, Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007

 <a id="4">[4]</a>
 Wes McKinney.
 <strong>Data Structures for Statistical Computing in Python</strong>,
 Proceedings of the 9th Python in Science Conference, 51-56 (2010)
 (<a class="reference external" href="http://conference.scipy.org/proceedings/scipy2010/mckinney.html">publisher link</a>)</p></li>

Fernando Pérez and Brian E. Granger.
<strong>IPython: A System for Interactive Scientific Computing</strong>,
Computing in Science &amp; Engineering, <strong>9</strong>, 21-29 (2007),
<a class="reference external" href="https://doi.org/10.1109/MCSE.2007.53">DOI:10.1109/MCSE.2007.53</a> (<a class="reference external" href="http://scitation.aip.org/content/aip/journal/cise/9/3/10.1109/MCSE.2007.53">publisher link</a>)
