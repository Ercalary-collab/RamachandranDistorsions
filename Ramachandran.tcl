
#Name of the output file    
set fp [ open "phi-psi.dat" w ]
set sel [ atomselect top "protein" ]
set n [ molinfo top get numframes]

for {set i 0 } { $i < $n } { incr i } {
    $sel frame $i
    $sel update
    puts $fp "\# frame: $i"

    set a [ $sel num ]
    for {set j 1 } { $j < $a } { incr j } {
            puts $fp "[lindex [$sel get {resname phi psi}] $j]"
        }
    }

$sel delete
close $fp 