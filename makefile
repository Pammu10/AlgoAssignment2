CXX = g++
CXXFLAGS = -O2 -std=c++17

ALGORITHMS = bubble insertion merge heap quickfirst quickrandom quickmedian radix

all: bin generate_inputs $(ALGORITHMS)

bin:
	mkdir -p bin

generate_inputs: main.cpp | bin
	$(CXX) $(CXXFLAGS) main.cpp -o bin/generate_inputs

$(ALGORITHMS): %: algorithms/%.cpp | bin
	$(CXX) $(CXXFLAGS) $< -o bin/$@

clean:
	rm -f bin/*