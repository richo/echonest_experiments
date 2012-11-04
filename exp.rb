#!/usr/bin/env ruby
require 'echonest'
require 'json'
require 'pry'

echonest = Echonest('LN2H7E4YGTZV2CQWQ')

ARGV.each do |filename|
  puts "Analysing #{filename}"
  analysis = echonest.track.analysis(filename)
  File.open("#{File.basename(filename)}.echonest", "w") do |f|
    puts "Writing analysis to #{File.basename(filename)}"
    f.puts analysis.json
  end
end
