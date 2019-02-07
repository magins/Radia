.PHONY: python clean

python: radia.so

radia.so:
	python setup.py build_ext --build-lib='../gcc'
	rm -rf build

clean:
	rm -rf build
	rm -f ../gcc/_radia*.so
