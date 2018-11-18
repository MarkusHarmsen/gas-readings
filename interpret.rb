require 'active_support/core_ext/time'

Time.zone = 'Europe/Berlin'

def readings(file)
  data = File.read file
  data = data.split("\n").map(&:to_f)

  step = 0.10
  value = nil

  data.map do |d|
    # Comments
    next if d.zero?

    # Reference value (negative)
    if d < 0
      value = (d * -1).round(1)
      next [nil, value]
    end

    # Actual data
    time = Time.zone.at(d)
    value = ((value || 0) + step).round(1) if value

    [time, value]
  end.compact
end

