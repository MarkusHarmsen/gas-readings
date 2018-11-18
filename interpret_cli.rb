require './interpret'

readings(ARGV[0]).each do |(time, value)|
  if time
    puts "#{time.strftime('%d.%m.%y %H:%M')}: #{value}"
  else
    puts value
  end
end

