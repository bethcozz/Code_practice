



gen anywarr=0
    replace anywarr=1 if capias==1
    replace anywarr=1 if warrant==1
label var anywarr "Either capias or other warrant"  

gen anyjail=0
    replace anyjail=1 if anywarr==1
    replace anyjail=1 if bond==1
label var anyjail "Either bond or warrant"

rename year yr  

gen caldate = date(date, "MDY")
format caldate %td
list
gen year = year(caldate)


gen startyr=yr

foreach num of numlist 10 11 12 13 14 15 {
replace startyr =20`num' if yr==`num'
}
*

foreach num of numlist 0 1 2 3 4 5 6 7 8 9 {
replace startyr = 200`num' if yr==`num'
}
*

foreach num of numlist 86 89 90 91 92 93 94 95 96 97 98 99 {
replace startyr =19`num' if yr==`num'
}
*

bysort id: egen numcapias = total(capias)
bysort ncp: egen numcapiasp = total(capias)



bysort id: egen numindigency = total(indigency)
bysort ncp: egen numindigencyp = total(indigency)
bysort id: egen numbond = total(bond)
bysort ncp: egen numbondp = total(bond)
bysort id: egen numwarrant = total(warrant)
bysort ncp: egen numwarrantp = total(warrant)
bysort id: egen numanywarr = total(anywarr)
bysort ncp: egen numanywarrp = total(anywarr)
bysort id: egen numrevoke = total(revoke)
bysort ncp: egen numrevokep = total(revoke)
bysort id: egen numappt = total(appt)
bysort ncp: egen numapptp = total(appt)
bysort id: egen numenf = total(enf)
bysort ncp: egen numenfp = total(enf)
bysort id: egen numnoservice = total(noservice)
bysort ncp: egen numnoservicep = total(noservice)
bysort id: egen numjail = total(anyjail)
bysort ncp: egen numjailp = total(anyjail)
bysort id: egen numunexeserv = total(unexeserv)
bysort ncp: egen numunexeservp = total(unexeserv)
bysort id: egen numgarnish = total(garnish)
bysort ncp: egen numgarnishp = total(garnish)


*N of events = 57,444 for 1,556 cases of 1,497 unique ncps*
logit anyjail numrevoke numenf numnoservice year, or cluster(id)
regress numjail indigency enf revoke noservice year, cluster(id)

logit anyjail startyr  numrevoke numenf numnoservice year, or cluster(id)

regress numjail indigency enf revoke noservice year, cluster(id)

tab capias
tab indigency
tab bond
tab warrant
tab anywarr
tab commit
tab cost
tab revoke
tab appt
tab enf
tab noservice

tab anywarr
tab anyjail


sum numcapias
sum numcapiasp
sum numindigency
sum numindigencyp
sum numbond
sum numbondp
sum numwarrant
sum numwarrantp
sum numanywarr
sum numanywarrp
sum numrevoke
sum numrevokep
sum numappt
sum numapptp
sum numenf
sum numenfp
sum numnoservice
sum numnoservicep
sum numjail
sum numjailp
sum numjail 
sum numjailp 
sum numunexeserv 
sum numunexeservp

tab numcapias
tab numcapiasp
tab numindigency
tab numindigencyp
tab numbond
tab numbondp
tab numwarrant
tab numwarrantp
tab numanywarr
tab numanywarrp
tab numrevoke
tab numrevokep
tab numappt
tab numapptp
tab numenf
tab numenfp
tab numnoservice
tab numnoservicep
tab numjail
tab numjailp
tab numjail 
tab numjailp 
tab numunexeserv 
tab numunexeservp

