function onTick()
	----
	Laser_Point = input.getNumber(1)
	state = input.getBool(2)
	y = input.getNumber(3)
	----
	output.setNumber(5, Laser_Point)
	output.setNumber(6, rotation)
	----
	http_body = "/"..Laser_Point.."|"..y.."|"..rotation
	if (state == false) then
		rotation = 1
		if (is_init == false) then
			stopSignal()
		end
	end

	if (state == true) then
		updateRotation()
		sendData(http_body)
		is_init = false
	end
end

function sendData(body)

	async.httpGet(10000, body)
end

function updateRotation()

	if (needReverse == false) then
		rotation = rotation + 0.01
		if (rotation >= 1) then
			needReverse = true
		end
	end

	if (needReverse == true) then
		rotation = rotation - 0.01
		if (rotation <= -1) then
			needReverse = false
		end
	end
end

function stopSignal()
	async.httpGet(10000, "/stop")
	is_init = true
end

function round(n)
    return n % 1 >= 0.5 and math.ceil(n) or math.floor(n)
end

rotation = 1
needReverse = false
is_init = true	
