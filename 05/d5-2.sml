fun read_list_of_number (file : string) =
  let
      val ins = TextIO.openIn file
      fun loopInt() =
	Option.valOf (TextIO.scanStream (Int.scan StringCvt.DEC) ins)
      fun loopList() =
	if TextIO.endOfStream ins then []
	else if TextIO.lookahead ins = SOME #"\n" then (TextIO.input1 ins; loopList())
	else loopInt() :: loopList()
  in
      loopList() before TextIO.closeIn ins
  end;


fun solve (start, x::xs, steps) =
  if x > length(xs) then steps+1
  else if x = 0 then solve(start, 1::xs, steps+1)
  else if x < 0 then solve(List.take(start, length(start)+x), List.drop(start,length(start)+x)@[x+1]@xs,steps+1)
  else if x > 2 then solve(start@[x-1]@List.take(xs, x-1), List.drop(xs,x-1),steps+1)
  else solve(start@[x+1]@List.take(xs, x-1), List.drop(xs,x-1),steps+1);

(fn () =>

    let
	val arr = read_list_of_number ("code");
    in
	print ("Answer: " ^ Int.toString(solve ([], arr, 0)) ^ "\n")
    end
)();
