studio = rws.getRobWorkStudio()
wc = studio:getWorkCell()
robot = wc:findDevice("PA10")
state = studio:getState()

function los()
  return math.random() * 6.28 - 3.14;
end

local clock = os.clock
function sleep(n)  -- seconds
  local t0 = clock()
  while clock() - t0 <= n do end
end

file = io.open("robo.csv", "w")

for i = 1,1000,1 do
  print("i=" .. i)

  q = rw.Q(7, los(), los(), los(), los(), los(), los(), los())
  robot:setQ(q, state)
  studio:setState(state)

  t = rw.worldTframe(robot:getEnd(), state)
  file:write(t:P()[0] .. ", " .. t:P()[1] .. ", " .. t:P()[2] .. "\n")

  sleep(0.1)
  --studio:saveViewGL("plik_" .. i .. ".png")
end

file:close()