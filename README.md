<p align="center">
  <img width="90%" src="https://github.com/jongablop/MinervaLab/blob/master/static/images/logo.png">
</p>

<p align="center">
A collection of interactive simulations of Thermodynamics and Statistical Physics.
</p>

### Try it now live:

- [Critical points](https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fcritical_points.ipynb)
- [effect of a and b](https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Feffect_of_a_and_b.ipynb)
- [Compare elements](https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fcompare_elements.ipynb)
- [Van der Waals p(v) 2D](https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fp_v_2D.ipynb)
- [Van der Waals p(v, T) 3D](https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fp_v_T_3D.ipynb)

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
            <td>#110-000</td>
            <td>Van der Waals equation of state</td>
            <td>apps/van_der_waals</td>
            <td>A collection of programs aimed to visualize the different aspects of the phase transitions of a gas that follows the Van der Waals equation of state.</td>
        </tr>
        <tr>
            <td>#111-000</td>
            <td>p(v, T) in 2D</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fp_v_2D.ipynb'>apps/van_der_waals/p_v_2D.ipynb</a></td>
            <td>A two-dimensional representation of the p(v,T) space during a gas-liquid phase transition (using reduced variables).</td>
        </tr>
        <tr>
            <td>#112-000</td>
            <td>change in volume</td>
            <td><a href='https://mybinder.org/v2/gh/jongablop/MinervaLab/master?urlpath=%2Fnotebooks%2Fapps%2Fvan_der_waals%2Fp_v_2D.ipynb'>apps/van_der_waals/p_v_2D.ipynb</a></td>
            <td>A two-dimensional representation of the p(v,T) space during a gas-liquid phase transition (using reduced variables).</td>
        </tr>
    </tbody>
</table>
</center>

## Dependencies:
+ `bqplot` (version = 0.11.6)
+ `ipywidgets`
+ `scipy`
+ `numpy`
+ `pip`
+ `matplotlib`
+ `qgrid`
+ `ipyvolume`

## License

This software is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE.md) file for details.
