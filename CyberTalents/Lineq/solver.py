#!/usr/bin/env python
a = [15345857135052644158,10107862342967460188,15514951512896411,4918093547848646552,9458472078791077712,10389810153032407159,10317166141181737080,4739071230119101568,5602877978471499087,6817739495547298027,6427678547440599488,9457480281190568299,3811243068786264022,775941643434169870,7024610526778714279,11651575732234344955,6625087805180364133,3669801280657684382,5443984100737085739,12346616364541216766,8986565623928863916,944611705353292388,9480419754515455118,6357470584650383564,4804105847411349449,]
f = [10753153698913165324,8412981602133999892,1482464683316586574,2025900790652430240,5398900907079313999,7029759589492702570,3468633932944308360,8675623443003281737,10322234074859615825,4437950083761802261,3279819731898553304,9305609025967996118,11526794456945961531,4738382726559211541,5323545124401969226,2873213552124115822,2787565658998643270,7567005815588497736,7873334411288369657,3904160665454908058,188593124624644258,5953933343058555785,13228205597299662061,3331190950406564692,9808705001033677355]
b = [15914389274045831441,12471333000718257439,11189085043185963643,14953553045254805869,16969044464796096757,12219369241978883401,11051035063490494121,12446419077417014895,17033822019842116078,9516363895804911673,15079736889469193431,10650632135951148921,17812647846133398533,11412472367550805013,9778393688778074575,16630642531754496501,9364964556418467329,14097382369878612419,10512797518085747507,15943449689777265613,18324134584075223407,11593718893451959913,14797616246348898583,10888050221402213645,15964574501738046999,]
import gmpy
for i in range(0,len(a)):
print chr(gmpy.divm(f[i],a[i], b[i]) % 256),
