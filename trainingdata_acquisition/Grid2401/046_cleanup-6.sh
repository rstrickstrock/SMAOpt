#! /bin/bash
cd experiments/

for directory in 0.3_*; do
  #echo $directory
  cd $directory

  mkdir density_results
  cd density/
  #rm batch_*
  #rm equilibrated.*
  #rm -rf force-field.ff
  #rm prod.cpt
  #rm prod_prev.cpt
  #rm prod.tpr
  #rm prod.trr
  mv density.xvg mdout.mdp prod.edr prod.gro prod.log slurm-* topol.top ../density_results
  cd ..
  rm -rf density
  
  mkdir energies_results
  cd energies/
  cd output/
  #rm *psi.leap.crd
  #rm *psi.leap.in
  #rm *psi.leap.log
  #rm *psi.leap.pdb
  #rm *psi.leap.top
  #rm *psi.min.rst
  #rm *psi.mol2
  #rm *psi.xyz
  mv Energy.* *psi.min.out ../../energies_results
  cd ..
  #rm batch_*
  #rm -rf bindir
  #rm ExTrM.template.dat
  #rm grow_sander_ff_opt.py
  #rm leap.log
  #rm leaprc.extrm
  #rm leaprc.extrm.w2p
  #rm mdinfo
  #rm molec.extrm.bcc.mol2
  #rm qmmm_eval.py
  #rm replace_placeholders.sh
  #rm run_mm.sh
  mv slurm-* ../energies_results
  cd ..
  rm -rf energies

  cd ..
done
