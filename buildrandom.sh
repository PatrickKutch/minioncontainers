cd random
rm -f -r  Board-Instrumentation-Framework
git clone https://github.com/intel/Board-Instrumentation-Framework.git
# don't need Marvin or Oscar
rm -r -f Board-Instrumentation-Framework/Oscar
rm -r -f Board-Instrumentation-Framework/Marvin
rm -r -f Board-Instrumentation-Framework/*.pdf

cd ..
docker build -t patrickkutch/biff-minion-random random
docker push patrickkutch/biff-minion-random

