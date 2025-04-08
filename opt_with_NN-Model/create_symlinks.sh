for dir in maxR2/maxR2-*
do
  cd $dir/energies/
  rm -rf bindir
  ln -s ../../../bindir/ .
  cd ../../../
  #echo $dir/energies/bindir
done

for dir in minMAPE/minMAPE-*
do
  cd $dir/energies/
  rm -rf bindir
  ln -s ../../../bindir/ .
  cd ../../../
  #echo $dir/energies/bindir
done
