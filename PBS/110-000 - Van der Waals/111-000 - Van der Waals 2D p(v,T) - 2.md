---
title: |
    \# 111-000\
    Van der Waals-en egoera ekuazioaren azterketa 2 dimentsiotan: p(v, T)\
    Data: 2019/09/16\
    Bertsioa: 1.0
---

Helburua
========

Programa honen helburua grafika interaktibo baten bitartez ikasleari Van
der Waals-en egoera ekuazio mekanikoan agertzen diren parametro zein
aldagaiek duten esangura fisikoataz jabetzea da. Aipaturiko aldagaiek
sistemaren fisikan duten eragina momentuan ikusteak lehen ebazteko
neketsuagoak ziren ariketak plantetzeko aukera ematen zaie irakasleei.\

Oinarri teorikoa
================

Honakoa da Van der Waals-en egoera ekuazio mekanikoa:

$$\label{van_der_waals}
\left( p + \frac{a}{v^2} \right) ( v- b) = RT \qquad \text{non} \qquad R = \text{gas idealen konstantea}$$

Sarritan, ekuazioaren forma laburtua erabiltzen da, batez ere
esanguratsuak diren adieazpen grafikoak lortzeko.

$$p_R = \frac{p}{p_c} \qquad v_R = \frac{v}{v_c} \qquad T_R = \frac{T}{T_c}$$

Aldagai erlatiboak definituz eta
[\[van\_der\_waals\]](#van_der_waals){reference-type="ref"
reference="van_der_waals"} ekuazioan ordezkatuz honako lortu dezakegu:

$$\label{van_der_waals_R}
\left( p_R + \frac{3}{v_R^2} \right) ( v_R - \frac{1}{3}) = \frac{8}{3} T_R$$

non $p_c$, $v_c$ eta $T_c$ gasaren presio, volumen eta
tenperatura-kritikoak diren, hurrenez-hurren:

$$p_C = \frac{1}{27} \frac{a}{b^2} \qquad v_c = 3b \qquad T_c = \frac{8}{27}\frac{a}{b}\frac{1}{R}$$

Sarritan lortutako
[\[van\_der\_waals\_R\]](#van_der_waals_R){reference-type="ref"
reference="van_der_waals_R"} ekuazioa erabiltzen da gas baten lerro
isotermoak grafikatzeko.

ETAB.

Garapena
========

-   \#111-001: Gas errealen parametroen datubasea.\
    Programak kargatuta izango ditu ohiko gasen $a$ eta $b$ parametroak.
    Horrela, modu azkar batean elementu ezberdinen izaeraren informazioa
    eskuragarri egongo da.

-   \#111-002: a eta b parametroak eskuz aldatzeko sliderrak.\
    $a$ eta $b$ parametroak eskuz aldatzeko aukera egongo da. Bi slider
    hauek \# 111-005 grafikara lotuta egongo dira eta momentuan ikusiko
    da parametro horiek aldatzearen eragina.

-   \#111-003: Tenperatura tartea aurkeratzeko textu-formularioak.\
    Kalkulatu nahi den tenperaturaren tartea, $T_c$-rekiko erlatiboki
    adierazita.

-   \#111-004: Grafika sortzeko botoia.\
    Grafika lehenengo aldiz generatzeko botoia. Hasieran hemendik
    beherako elementu guztiak ez dira ikusgai egongo eta hau lehenengo
    aldiz sakatzean agertuko dira. Honek erabiltzailearen atentzioa
    bideratzea du helburu.

-   \#111-005: p(v,T) planoaren grafika.\
    Grafika honetan une horretan lan egiten ari zaren lerro isotermoa,
    gordetako isoterma guztiak eta isoterma horietan gordetako
    markadoreak agertuko dira. Gainera, Maxwell-en 'construction'-eko
    lerro horizontala (isoterma erreala lortzeko erabiltzen dena)
    agertuko da eta zuzen hori eta lerro isotermaren arteko azalera
    koloreztatuta agertuko da.

-   \#111-006: Lerro isoterma ezberdinekin lan egiteko slider-a.\
    Sliderrak une batean lan egiten ari garen lerro isotermoaren
    tenperatura aldatzeko balioko du.

-   \#111-007: Lerro isotermaren tenperatura.\
    Une batean lan egiten ari garen lerro isotermoaren tenperatura
    adieraziko du. \#111-006: elementuarekin lotuta egongo da.

-   \#111-008: Kalkulatutako isoterma guztiak erakusteko checkbox-a.\
    Aktibatuta dagoenean \#111-003 elementuan aukeratutako tartean
    kalkulatutako isoterma guztiak erakutsiko dira.\
    *Zenbat isoterma kalkulatu behar diren aukeratzeko textu formulario
    bat jarri beharko litzateke.*

-   \#111-009: Isotermak gordetzeko botoiak.\
    Lan egiten ari zaren isoterma gordetzeko edota gordetako azkena
    baztertzeko botoiak.

-   \#111-00A: Isoterman 'tracer' bat erakusteko checkbox-a eta hori
    mugitzeko slider-a.\
    Checkbox-a aktibatzean une horretan lan egiten ari garen isoterman
    puntu bat agertuko da, sliderraren bitartez isoterman zehar mugitu
    ahalko dena.

-   \#111-00B: Marka bat gehitzeko formularioa.\
    Botoiari sakatzean textu formularioan jasotako izena duen puntu bat
    markatuko da 'tracer'-a dagoen tokian.\
    *Markak kentzeko botoi bat eta dropdown bat jarri beharko ziren.*

-   \#111-00C: 'Maxwell contruction' (palankaren erregela) erakusteko
    checkbox-a.\
    Aktibatzean palankaren erregelaren erlazionatutako elementuak
    ikusiko dira \#111-005 grafikan (presio konstanteko zuzena eta
    koloreztatutako azalerak, azken hauek aktibatuta badaude).

-   \#111-00D: presio konstanteko zuzena mugitzeko sliderra.\

-   \#111-00E: Isotermaren eta presio konstanteko lerroaren arteko
    azalerak koloreztatzeko checkbox-a.\
    Aktibatzean aipaturiko azalerak koloreztatuko dira.

-   \#111-00F: Isotermaren eta presio konstanteko lerroaren arteko
    azaleren balioak adierazteko textuak.\
    Isotermaren eta presio konstanteko lerroaren arteko azaleren balioak
    agertuko dira: zuzenak aldapa konstanteko isotermaren zatia mozten
    duenetik ezkerrera gelditzen denaren azalera, bertatik eskubira
    gelditzen deneko azalera eta bien batura.\
    Integral guztiak analitikoki ebatziko dira.\

-   \#111-010: Isoterma erreala kalkulatzeko botoia.\
    Sakatzean, programa arduratuko da presio ezberdinetarako integralak
    burutzeaz eta integrala 0 deneko presioa topatzeaz. Agian, prozedura
    grafikan ikusi daiteke.

-   \#111-011: Irudia exportatzeko botoia.\
    Sakatzean lortutako irudia formatu ezberdinetara exportatzea
    ahalbdeituko duen menu bat agertuko da.
