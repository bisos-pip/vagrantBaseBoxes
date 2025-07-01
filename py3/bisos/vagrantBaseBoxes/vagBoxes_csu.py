# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= as equivalent of facter in py and remotely with rpyc.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/facter/py3/bisos/facter/facter_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['facter_csu'], }
csInfo['version'] = '202403270908'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'facter_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
This a =Cs-Unit= for running the equivalent of facter in py and remotely with rpyc.
With BISOS, it is used in CMDB remotely.

** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= "  :title "*Py Library IMPORTS*" :comment "-- Framework and External Packages Imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- Framework and External Packages Imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# import os
import collections
# import pathlib
# import invoke

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import __main__ 

from bisos.debian import configFile

from bisos.vagrantBaseBoxes import vagBoxPathInfo

from pprint import pprint

import pathlib

from datetime import datetime

####+BEGIN: b:py3:cs:orgItem/basic :type "=Executes=  "  :title "CSU-Lib Executions" :comment "-- cs.invOutcomeReportControl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Executes=   [[elisp:(outline-show-subtree+toggle)][||]] CSU-Lib Executions -- cs.invOutcomeReportControl  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

cs.invOutcomeReportControl(cmnd=True, ro=True)

####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    pass


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Direct Command Services" :anchor ""  :extraInfo "Examples and CSs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Direct Command Services_: |]]  Examples and CSs  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :comment "" :parsMand "" :parsOpt "perfName" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_csu>>  =verify= parsOpt=perfName ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             perfName: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'perfName': perfName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        perfName = csParam.mappedValue('perfName', perfName)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        cs.examples.menuChapter('=Direct Interface Commands=')

        oneVagBoxPath = "/bisos/git/bxRepos/bxObjects/bro_vagrantDebianBaseBoxes/qemu/debian/13/trixie/amd64/netinst/us.pkr.hcl"

        forceModePars = od([('force', 't'),])

        cmnd('vagBoxPath_obtain',  args=oneVagBoxPath)

        cs.examples.menuSection('/vagBoxPath --- Discrete Commands/')

        cmnd('vagBoxPath_build',  args=oneVagBoxPath)
        cmnd('vagBoxPath_add',  args=oneVagBoxPath)
        cmnd('vagBoxPath_add', pars=forceModePars, args=oneVagBoxPath)
        cmnd('vagBoxPath_run',  args=oneVagBoxPath)
        cmnd('vagBoxPath_clean',  args=oneVagBoxPath)

        cs.examples.menuSection('/vagBoxPath --- Compound Commands/')

        cmnd('vagBoxPath_buildAdd',  args=oneVagBoxPath)
        cmnd('vagBoxPath_buildAdd', pars=forceModePars, args=oneVagBoxPath)
        cmnd('vagBoxPath_buildAddClean',  args=oneVagBoxPath)
        cmnd('vagBoxPath_buildAddClean', pars=forceModePars, args=oneVagBoxPath)

        cs.examples.menuSection('/Commands for Development/')

        cmnd('cmndDevExamples')

        cs.examples.menuChapter('=Related Commands=')

        literal("vagrantBaseBoxes-sbom")

        return(cmndOutcome)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "cmndDevExamples" :comment "" :parsMand "" :parsOpt "perfName" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<cmndDevExamples>>  =verify= parsOpt=perfName ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class cmndDevExamples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'perfName', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             perfName: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'perfName': perfName, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        perfName = csParam.mappedValue('perfName', perfName)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Development example command.
        #+end_org """)

        configFile.examples_csu(concreteConfigFile='vagBoxAddJson', sectionTitle="default")

        return(cmndOutcome)


####+BEGIN: b:py3:cs:func/typing :funcName "boxFileNameFromInfo" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /boxFileNameFromInfo/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def boxFileNameFromInfo(
####+END:
) -> str:
    boxPathInfo = vagBoxPathInfo.boxPathInfo
    return (
        f"{boxPathInfo.distro}-{boxPathInfo.distroRel}-{boxPathInfo.cpuArch}-{boxPathInfo.provider}.box"
    )

####+BEGIN: b:py3:cs:func/typing :funcName "boxFileAbsPathFromInfo" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /boxFileAbsPathFromInfo/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def boxFileAbsPathFromInfo(
####+END:
) -> pathlib.Path:
    boxPathInfo = vagBoxPathInfo.boxPathInfo
    boxFileName = boxFileNameFromInfo()
    boxFileAbsPath = boxPathInfo.boxBaseDir.joinpath(boxFileName)
    return boxFileAbsPath


####+BEGIN: b:py3:cs:func/typing :funcName "boxNameFromInfo" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /boxNameFromInfo/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def boxNameFromInfo(
####+END:
) -> str:
    boxPathInfo = vagBoxPathInfo.boxPathInfo
    return (
        f"{boxPathInfo.creator}/{boxPathInfo.distro}-{boxPathInfo.distroVersion}-{boxPathInfo.cpuArch}/{boxPathInfo.boxCapability}/{boxPathInfo.selector}"
    )

####+BEGIN: b:py3:cs:func/typing :funcName "boxAddJsonFileNameFromInfo" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /boxAddJsonFileNameFromInfo/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def boxAddJsonFileNameFromInfo(
####+END:
) -> str:
    boxPathInfo = vagBoxPathInfo.boxPathInfo
    return (
        f"{boxPathInfo.distro}-{boxPathInfo.distroRel}-{boxPathInfo.cpuArch}-{boxPathInfo.provider}.boxAdd.json"
    )

####+BEGIN: b:py3:cs:func/typing :funcName "boxAddJsonFileAbsPathFromInfo" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /boxAddJsonFileAbsPathFromInfo/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def boxAddJsonFileAbsPathFromInfo(
####+END:
) -> pathlib.Path:
    boxPathInfo = vagBoxPathInfo.boxPathInfo
    boxAddJsonFileName = boxAddJsonFileNameFromInfo()
    boxAddJsonFileAbsPath = boxPathInfo.boxBaseDir.joinpath(boxAddJsonFileName)
    return boxAddJsonFileAbsPath


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vagBoxPath_obtain" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vagBoxPath_obtain>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vagBoxPath_obtain(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns runFacterAndGetJsonOutputBytes.
        #+end_org """)

        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  facter.cs -i factName networking.primary # os.distro.id
#+end_src
#+RESULTS:
: [{'networking.primary': 'enp1s0'}]

#+begin_src sh :results output :session shared
  facter-roInv.cs --perfName="HSS-1012" -i factName networking.primary os.distro.id
#+end_src
#+RESULTS:
: Performing: factName () {'cache': 'True', 'fromFile': None, 'perfName': 'HSS-1012', 'argsList': ['networking.primary', 'os.distro.id'], 'rtInv': <bisos.b.cs.rtInvoker.RtInvoker object at 0x7fe0c4de2310>, 'cmndOutcome': <bisos.b.op.Outcome object at 0x7fe0c4de2590>}
: Performer Outcome:: [{'networking.primary': 'eno1'}, {'os.distro.id': 'Debian'}]
: [{'networking.primary': 'eno1'}, {'os.distro.id': 'Debian'}]


        #+end_org """)

        vagBoxPkrFileStr = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        boxPathInfo = vagBoxPathInfo.vagBoxPathExtractInfo(pathlib.Path(vagBoxPkrFileStr))

        if boxPathInfo is None:
            return failed(cmndOutcome, f"Missing {vagBoxPkrFileStr}")

        if rtInv.outs:
            # b_io.tm.here(f"configFilePath")
            pprint(vars(boxPathInfo))

            boxFileName = boxFileNameFromInfo()
            print(f"boxFileName = {boxFileName}")

            boxFileAbsPath = boxFileAbsPathFromInfo()
            print(f"boxFileAbsPath = {boxFileAbsPath}")

            boxName = boxNameFromInfo()
            print(f"boxName = {boxName}")

        return cmndOutcome.set(opResults=boxPathInfo,)


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="vagBoxPath",
            argDefault='',
            argChoices=[],
            argDescription="One argument, any string for vagBoxPath"
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vagBoxPath_build" :extent "verify" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vagBoxPath_build>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vagBoxPath_build(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Return a dict of parName:parValue as results
        #+end_org """)

        vagBoxPkrFileStr = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        boxPathInfo = vagBoxPathInfo.vagBoxPathExtractInfo(pathlib.Path(vagBoxPkrFileStr))

        if boxPathInfo is None:
            return failed(cmndOutcome, f"Missing {vagBoxPkrFileStr}")

        boxBaseDir = boxPathInfo.boxBaseDir

        boxFileName = boxFileNameFromInfo()
        boxFilePath = boxBaseDir.joinpath(boxFileName)

        if boxFilePath.is_file():
            boxFilePath.unlink()

        if b.subProc.Op(outcome=cmndOutcome,
                        cd=boxBaseDir,
                        log=1).bash(
f"""env \
        CHECKPOINT_DISABLE=1 \
	    PACKER_LOG=1 \
	    PACKER_LOG_PATH={boxFileName}.init.log \
        packer init {boxPathInfo.selector}.pkr.hcl"""
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        if b.subProc.Op(outcome=cmndOutcome,
                        cd=boxBaseDir,
                        log=1).bash(
f"""env \
        PACKER_KEY_INTERVAL=10ms \
	    CHECKPOINT_DISABLE=1 \
	    PACKER_LOG=1 \
	    PACKER_LOG_PATH={boxFileName}.log \
	    PKR_VAR_version={boxPathInfo.distroRel} \
	    PKR_VAR_vagrant_box={boxFileName} \
		packer build -on-error=abort -timestamp-ui {boxPathInfo.selector}.pkr.hcl"""
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        # -only=qemu.debian-amd64 
        
        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="vagBoxPath",
            argDefault='',
            argChoices=[],
            argDescription="One argument, any string for vagBoxPath"
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vagBoxPath_add" :extent "verify" :parsMand "" :parsOpt "force" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vagBoxPath_add>>  =verify= parsOpt=force argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vagBoxPath_add(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'force', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             force: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'force': force, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        force = csParam.mappedValue('force', force)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Return a dict of parName:parValue as results
        #+end_org """)

        vagBoxPkrFileStr = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        boxPathInfo = vagBoxPathInfo.vagBoxPathExtractInfo(pathlib.Path(vagBoxPkrFileStr))

        if boxPathInfo is None:
            return failed(cmndOutcome, f"Missing {vagBoxPkrFileStr}")

        forceStr = ""
        if force is not False:
            forceStr = " -f "

        boxBaseDir = boxPathInfo.boxBaseDir

        boxFileName = boxFileNameFromInfo()
        boxFilePath = boxBaseDir.joinpath(boxFileName)

        if not boxFilePath.is_file():
            return failed(cmndOutcome, f"Missing {boxFilePath}")

        boxName = boxNameFromInfo()

        # __main__ provides for automation configFile  menu/examples
        __main__.vagBoxAddJson.configFileUpdate()

        boxAddJsonFileAbsPath = boxAddJsonFileAbsPathFromInfo()
        if not boxAddJsonFileAbsPath.is_file():
            return failed(cmndOutcome, f"Missing {boxAddJsonFileAbsPath}")


        if b.subProc.Op(outcome=cmndOutcome,
                        log=1).bash(
f"""vagrant box add {forceStr} --name "{boxName}" {boxAddJsonFileAbsPath}"""
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="vagBoxPath",
            argDefault='',
            argChoices=[],
            argDescription="One argument, any string for vagBoxPath"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vagBoxPath_add_withName_OBSOLETED" :extent "verify" :parsMand "" :parsOpt "force" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vagBoxPath_add_withName_OBSOLETED>>  =verify= parsOpt=force argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vagBoxPath_add_withName_OBSOLETED(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'force', ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             force: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'force': force, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        force = csParam.mappedValue('force', force)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Return a dict of parName:parValue as results
        #+end_org """)

        vagBoxPkrPathStr = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        boxPathInfo = vagBoxPathInfo.vagBoxPathExtractInfo(pathlib.Path(vagBoxPkrPathStr))

        if boxPathInfo is None:
            return failed(cmndOutcome, f"Missing {vagBoxPkrPathStr}")

        forceStr = ""
        if force is not False:
            forceStr = " -f "

        boxBaseDir = boxPathInfo.boxBaseDir

        boxFileName = f"{boxPathInfo.distro}-{boxPathInfo.distroRel}-{boxPathInfo.cpuArch}-{boxPathInfo.provider}.box"
        boxFilePath = boxBaseDir.joinpath(boxFileName)

        if not boxFilePath.is_file():
            return failed(cmndOutcome, f"Missing {boxFilePath}")

        boxName = f"{boxPathInfo.creator}/{boxPathInfo.distro}-{boxPathInfo.distroVersion}-{boxPathInfo.cpuArch}/{boxPathInfo.boxCapability}/{boxPathInfo.selector}"

        if b.subProc.Op(outcome=cmndOutcome,
                        log=1).bash(
f"""vagrant box add {forceStr} --name "{boxName}" --provider {boxPathInfo.provider} {boxFilePath}"""
        ).isProblematic():  return(b_io.eh.badOutcome(cmndOutcome))

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="vagBoxPath",
            argDefault='',
            argChoices=[],
            argDescription="One argument, any string for vagBoxPath"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vagBoxPath_clean" :extent "verify" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vagBoxPath_clean>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vagBoxPath_clean(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Return a dict of parName:parValue as results
        #+end_org """)

        vagBoxPkrFileStr = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        boxPathInfo = vagBoxPathInfo.vagBoxPathExtractInfo(pathlib.Path(vagBoxPkrFileStr))

        if boxPathInfo is None:
            return failed(cmndOutcome, f"Missing {vagBoxPkrFileStr}")

        boxBaseDir = boxPathInfo.boxBaseDir

        boxFileName = boxFileNameFromInfo()
        boxFilePath = boxBaseDir.joinpath(boxFileName)

        if boxFilePath.is_file():
            boxFilePath.unlink()

        boxFileInitLog = boxBaseDir.joinpath(f"{boxFileName}.init.log")
        if boxFileInitLog.is_file():
            boxFileInitLog.unlink()

        boxFileLog = boxBaseDir.joinpath(f"{boxFileName}.log")
        if boxFileLog.is_file():
            boxFileLog.unlink()

        boxAddJsonFile = boxAddJsonFileAbsPathFromInfo()
        if boxAddJsonFile.is_file():
            boxAddJsonFile.unlink()

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="vagBoxPath",
            argDefault='',
            argChoices=[],
            argDescription="One argument, any string for vagBoxPath"
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vagBoxPath_buildAdd" :extent "verify" :parsMand "force" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vagBoxPath_buildAdd>>  =verify= parsMand=force argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vagBoxPath_buildAdd(cs.Cmnd):
    cmndParamsMandatory = [ 'force', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             force: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'force': force, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        force = csParam.mappedValue('force', force)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Return a dict of parName:parValue as results
        #+end_org """)

        vagBoxPkrFileStr = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        boxPathInfo = vagBoxPathInfo.vagBoxPathExtractInfo(pathlib.Path(vagBoxPkrFileStr))

        if boxPathInfo is None:
            return failed(cmndOutcome, f"Missing {vagBoxPkrFileStr}")

        if vagBoxPath_build().pyCmnd(
                argsList=[vagBoxPkrFileStr,],
        ).isProblematic(): return(b_io.eh.badOutcome(cmndOutcome))

        if vagBoxPath_add().pyCmnd(
                force=force,
                argsList=[vagBoxPkrFileStr,],
        ).isProblematic(): return(b_io.eh.badOutcome(cmndOutcome))

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="vagBoxPath",
            argDefault='',
            argChoices=[],
            argDescription="One argument, any string for vagBoxPath"
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vagBoxPath_buildAddClean" :extent "verify" :parsMand "force" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vagBoxPath_buildAddClean>>  =verify= parsMand=force argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vagBoxPath_buildAddClean(cs.Cmnd):
    cmndParamsMandatory = [ 'force', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             force: typing.Optional[str]=None,  # Cs Mandatory Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'force': force, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        force = csParam.mappedValue('force', force)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Return a dict of parName:parValue as results
        #+end_org """)

        vagBoxPkrFileStr = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        boxPathInfo = vagBoxPathInfo.vagBoxPathExtractInfo(pathlib.Path(vagBoxPkrFileStr))

        if boxPathInfo is None:
            return failed(cmndOutcome, f"Missing {vagBoxPkrFileStr}")

        if vagBoxPath_build().pyCmnd(
                argsList=[vagBoxPkrFileStr,],
        ).isProblematic(): return(b_io.eh.badOutcome(cmndOutcome))

        if vagBoxPath_add().pyCmnd(
                force=force,
                argsList=[vagBoxPkrFileStr,],
        ).isProblematic(): return(b_io.eh.badOutcome(cmndOutcome))

        if vagBoxPath_buildAddClean().pyCmnd(
                force=force,
        ).isProblematic(): return(b_io.eh.badOutcome(cmndOutcome))

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="vagBoxPath",
            argDefault='',
            argChoices=[],
            argDescription="One argument, any string for vagBoxPath"
        )

        return cmndArgsSpecDict

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Config File Classes" :anchor ""  :extraInfo "Vagrant Box Add Json Config File"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Config File Classes_: |]]  Vagrant Box Add Json Config File  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:class/decl :className "ConfigFile_vagBoxAddJson" :superClass "configFile.ConfigFile" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /ConfigFile_vagBoxAddJson/  superClass=configFile.ConfigFile  [[elisp:(org-cycle)][| ]]
#+end_org """
class ConfigFile_vagBoxAddJson(configFile.ConfigFile):
####+END:
    """ #+begin_org
** [[elisp:(org-cycle)][| DocStr| ]]  InMail Service Access Instance Class for an Accessible Abstract Service.
    #+end_org """

####+BEGIN: b:py3:cs:method/typing :methodName "configFilePath" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /configFilePath/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def configFilePath(
####+END:
            self,
    ) -> pathlib.Path:
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Return path
        #+end_org """

        pkrFileAbsPath = vagBoxPathInfo.boxPathInfo.pkrFileAbsPath
        if pkrFileAbsPath is None:
            cnfgFilePath = pathlib.Path("invalid_configFilePath__boxPathInfo_haNotBeenSet")
            return cnfgFilePath

        cnfgFilePath = boxAddJsonFileAbsPathFromInfo()
        return cnfgFilePath

####+BEGIN: b:py3:cs:method/typing :methodName "configFileStr" :methodType "" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-     [[elisp:(outline-show-subtree+toggle)][||]] /configFileStr/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def configFileStr(
####+END
            self,
    ) -> str:
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Returns string
Taken from https://github.com/rgl/debian-vagrant/blob/master/box-metadata.sh
-------------
# see https://developer.hashicorp.com/vagrant/docs/boxes/format#box-metadata
# see https://developer.hashicorp.com/vagrant/docs/boxes/format#box-file
# see https://github.com/hashicorp/packer-plugin-vagrant/blob/v1.1.4/post-processor/vagrant/libvirt.go#L105-L109
# see https://github.com/vagrant-libvirt/vagrant-libvirt/blob/0.11.2/spec/unit/action/handle_box_image_spec.rb#L96-L125
# see https://github.com/vagrant-libvirt/vagrant-libvirt/blob/0.11.2/lib/vagrant-libvirt/action/handle_box_image.rb
# see https://github.com/vagrant-libvirt/vagrant-libvirt/blob/0.11.2/docs/boxes.markdown
-----------
        #+end_org """

        boxPathInfo = vagBoxPathInfo.boxPathInfo
        if boxPathInfo.distro is None:
            vagBoxName = "invalid_vagBoxName"
            vagBoxVer = "invalid_vagBoxVer"
            vagProvider = "invalid_vagProvider"
            vagBoxPath = "invalid_vagBoxPath"
        else:
            vagBoxName = boxNameFromInfo()
            vagBoxVer = datetime.now().strftime('%Y%m%d')
            vagProvider = boxPathInfo.provider
            vagBoxPath = boxFileAbsPathFromInfo()

        templateStr = f"""\
{{
  "name": "{vagBoxName}",
  "versions": [
    {{
      "version": "{vagBoxVer}",
      "providers": [
        {{
          "name": "{vagProvider}",
          "url": "{vagBoxPath}"
        }}
      ]
    }}
  ]
}}
"""
        return templateStr


####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
