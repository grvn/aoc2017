var goal = prompt("Please enter the goal", "277678");
var start = 1;
var current = 1;
var matrix = {};
var dir = new Point(1,0);
var point = new Point(0,0);
var steps = 1;
var taken = 0;
var x = 0;

do{
    matrix[point.x+":"+point.y] = current;
    point.x+=dir.x;
    point.y+=dir.y;
    current = ( matrix[(point.x+1)+":"+(point.y)] != null )?matrix[(point.x+1)+":"+(point.y)]:0;
    current +=( matrix[(point.x+1)+":"+(point.y+1)] != null )?matrix[(point.x+1)+":"+(point.y+1)]:0;
    current +=( matrix[(point.x)+":"+(point.y+1)] != null )?matrix[(point.x)+":"+(point.y+1)]:0;
    current +=( matrix[(point.x-1)+":"+(point.y+1)] != null )?matrix[(point.x-1)+":"+(point.y+1)]:0;
    current +=( matrix[(point.x-1)+":"+(point.y)] != null )?matrix[(point.x-1)+":"+(point.y)]:0;
    current +=( matrix[(point.x-1)+":"+(point.y-1)] != null )?matrix[(point.x-1)+":"+(point.y-1)]:0;
    current +=( matrix[(point.x)+":"+(point.y-1)] != null )?matrix[(point.x)+":"+(point.y-1)]:0;
    current +=( matrix[(point.x+1)+":"+(point.y-1)] != null )?matrix[(point.x+1)+":"+(point.y-1)]:0;
    taken++;
    if(taken >= steps){
	turn(dir);
	taken = 0;
	x++;
	if(x==2){
	    steps++;
	    x=0;
	}
    }
    

}while(current <= goal);

alert(`Answer: ${current}`);

function Point(x, y) {
    this.x = x;
    this.y = y;
}

function turn(p){
    if(p.x==0 && p.y==1){p.x=-1;p.y=0;}
    else if(p.x==1 && p.y==0){p.x=0;p.y=1;}
    else if(p.x==0 && p.y==-1){p.x=1;p.y=0;}
    else if(p.x==-1 && p.y==0){p.x=0;p.y=-1;}
}
