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
    while($input =~ m/</){
	my $old = length $input;
	$input =~ s/<([^>]*)>//;
	$score += ($old - length($input) - 2);
    }
    print $score."\n";
}
