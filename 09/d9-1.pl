#!/usr/bin/perl

use strict;
use warnings;
use autodie;
use Path::Tiny;


while(<STDIN>){
    my $score = 0;
    chomp($_);
    my $input = path($_)->slurp_utf8;
    $input =~ s/\!.//g;
    $input =~ s/,//g;
    $input =~ s/<([^>]*)>//g;
    my $multiplier = 0;
    foreach my $char (split('', $input)){
	if($char eq "{"){
	    $score += ++$multiplier;
	}
	if($char eq "}"){
	    $multiplier--;
	}
    }
    print $score."\n";
}
