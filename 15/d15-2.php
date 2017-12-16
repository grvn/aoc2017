<?php
$facA=16807;
$facB=48271;
$div=(2**31)-1;
$modA=4;
$modB=8;
$sig_bits=(2**16)-1;
$loop=5000000;
$matches=0;
//$sA=65;
//$sB=8921;
$sA=679;
$sB=771;
for($i=0;$i<$loop;$i++){
    $sA=generate($modA,$sA,$facA,$div);
    $sB=generate($modB,$sB,$facB,$div);
    if(($sA & $sig_bits) == ($sB & $sig_bits)){
        $matches++;
    }
}
echo "Answer: ".$matches;

function generate($mod,$start,$fac,$div){
    do {
        $start=($start*$fac)%$div;        
    } while ($start%$mod!=0);
    return $start;
}
?>
