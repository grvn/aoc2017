var steps = 0;
var count = 1;
var goal = prompt("Please enter the goal", "277678");
var quot = 0;
var diff = 0;
if(goal > 1){
    while(count < goal) {
	steps++;
	count = steps*8 + count;
    }
    quot=Math.floor((count-goal)/(steps));
    diff=((count-goal)%(steps));
}
else
{
    alert(`Answer: 0`);
}
if(quot%2==0){
    alert(`Answer: ${steps+(steps-diff)}`);
}
else{
    alert(`Answer: ${steps+diff}`);
}
