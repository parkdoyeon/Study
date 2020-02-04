num = 100
:timer.tc(fn ->
    for x<-1..num, y<-x+1..num, z<-y+1..num, x*x+y*y==z*z, do: [x, y, z]
end)
|> IO.inspect charlists: :as_lists
