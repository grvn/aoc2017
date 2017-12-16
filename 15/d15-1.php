<?php
$facA=16807;
$facB=48271;
$div=(2**31)-1;
$sig_bits=(2**16)-1;
$loop=40000000;
$matches=0;
//$sA=65;
//$sB=8921;
$sA=679;
$sB=771;
for($i=0;$i<$loop;$i++){
    $sA=($sA*$facA)%$div;
    $sB=($sB*$facB)%$div;
    if(($sA & $sig_bits) == ($sB & $sig_bits)){
        $matches++;
    }
}
echo "Answer: ".$matches;

?>
