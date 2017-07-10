-- DROP
drop trigger compito_incr;
drop trigger domanda_incr;
drop trigger figura_incr;
drop trigger risposta_incr;
drop trigger prova_incr;
drop trigger esami_sostenuti_incr;
drop trigger check_compito;
drop trigger check_corretta;
drop trigger check_insegnamento;
drop trigger check_prova;
drop trigger update_insegnamento;
drop trigger check_esami_sostenuti;
drop trigger valuta_risposte_chiuse;
drop trigger update_esami_superati;
drop trigger check_domanda_aperta;
drop trigger check_ref_esami_sostenuti;
drop trigger check_ref_prova;
drop trigger check_nt_compito;
drop trigger check_duplicati_nt_domande;
drop trigger check_duplicati_nt_figure;
drop trigger check_duplicati_nt_compito;
drop trigger check_unique_prova;
drop trigger check_domande_prova;
drop trigger check_risposte_prova;

drop table insegnamento;
drop table figura;
drop table risposta;
drop table domanda;
drop table compito;
drop table studente;
drop table esami_sostenuti;
drop table prova;

drop type insegnamentoty force;
drop type figuraty force;
drop type rispostaty force;
drop type risposta_chiusaty force;
drop type risposta_apertaty force;
drop type domandaty force;
drop type ref_figurety force;
drop type ref_figurent force;
drop type domanda_chiusaty force;
drop type ref_rispostety force;
drop type ref_rispostent force;
drop type domanda_apertaty force;
drop type compitoty force;
drop type ref_domandety force;
drop type ref_domandent force;
drop type studentety force;
drop type esami_sostenutity force;
drop type provaty force;

drop sequence figura_seq;
drop sequence risposta_seq;
drop sequence domanda_seq;
drop sequence compito_seq;
drop sequence prova_seq;
drop sequence esami_sostenuti_seq;

-- TIPI
create type insegnamentoty as object(
	codice integer,
	nome varchar2(20),
	numesamisostenuti integer,
	numesamisuperati integer
) final;
/
create type figuraty as object(
	id integer,
	descrizione varchar2(20)
) final;
/
create type rispostaty as object(
	id integer,
	testo varchar2(50),
	tipo varchar2(25),
	constructor function rispostaty(self in out nocopy rispostaty, testo varchar2) return self as result
) not final;
/
create type body rispostaty is
	constructor function rispostaty(self in out nocopy rispostaty, testo varchar2) return self as result is
	begin
		self.id := 1;
		self.testo := testo;
		self.tipo := 'risposta';
		return;
	end;
end;
/
create type risposta_chiusaty under rispostaty(
	constructor function risposta_chiusaty(self in out nocopy risposta_chiusaty, testo varchar2) return self as result
) final;
/
create type body risposta_chiusaty is
	constructor function risposta_chiusaty(self in out nocopy risposta_chiusaty, testo varchar2) return self as result is
	begin
		self.id := 1;
		self.testo := testo;
		self.tipo := 'risposta_chiusa';
		return;
	end;
end;
/
create type risposta_apertaty under rispostaty(
	constructor function risposta_apertaty(self in out nocopy risposta_apertaty, testo varchar2) return self as result
) final;
/
create type body risposta_apertaty is
	constructor function risposta_apertaty(self in out nocopy risposta_apertaty, testo varchar2) return self as result is
	begin
		self.id := 1;
		self.testo := testo;
		self.tipo := 'risposta_aperta';
		return;
	end;
end;
/
create type ref_figurety as object(
	figura ref figuraty
);
/
create type ref_figurent as table of ref_figurety;
/
create type ref_rispostety as object(
	risposte ref risposta_chiusaty,
	corretta number(1)
);
/
create type ref_rispostent as table of ref_rispostety;
/
create type domandaty as object(
	id integer,
	testo varchar2(50),
	punteggio integer,
	tipo varchar2(25),
 	figure ref_figurent,
    risposte ref_rispostent,
	constructor function domandaty(self in out nocopy domandaty, testo varchar2, punteggio integer, figure ref_figurent, risposte ref_rispostent) return self as result
) not final;
/
create type body domandaty is
	constructor function domandaty(self in out nocopy domandaty, testo varchar2, punteggio integer, figure ref_figurent, risposte ref_rispostent) return self as result is
	begin
		self.id := 1;
		self.testo := testo;
		self.punteggio := punteggio;
		self.figure := figure;
		self.risposte := risposte;
		self.tipo := 'domanda';
		return;
	end;
end;
/
create type domanda_chiusaty under domandaty(
	constructor function domanda_chiusaty(self in out nocopy domanda_chiusaty, testo varchar2, punteggio integer, figure ref_figurent, risposte ref_rispostent) return self as result
) final;
/
create type body domanda_chiusaty is
	constructor function domanda_chiusaty(self in out nocopy domanda_chiusaty, testo varchar2, punteggio integer, figure ref_figurent, risposte ref_rispostent) return self as result is
	begin
		self.id := 1;
		self.testo := testo;
		self.punteggio := punteggio;
		self.figure := figure;
		self.risposte := risposte;
		self.tipo := 'domanda_chiusa';
		return;
	end;
end;
/
create type domanda_apertaty under domandaty(
	constructor function domanda_apertaty(self in out nocopy domanda_apertaty, testo varchar2, punteggio integer, figure ref_figurent) return self as result
) final;
/
create type body domanda_apertaty is
	constructor function domanda_apertaty(self in out nocopy domanda_apertaty, testo varchar2, punteggio integer, figure ref_figurent) return self as result is
	begin
		self.id := 1;
		self.testo := testo;
		self.punteggio := punteggio;
		self.figure := figure;
		self.risposte := null;
		self.tipo := 'domanda_aperta';
		return;
	end;
end;
/
create type ref_domandety as object(
	domanda ref domandaty
);
/
create type ref_domandent as table of ref_domandety;
/
create type compitoty as object(
	id integer,
	docente varchar2(20),
	insegnamento ref insegnamentoty,
	data date,
	num_domande integer,
	domande ref_domandent
) final;
/
create type studentety as object(
	matricola integer,
	cognome varchar2(20),
	numEsamiSuperati integer
) final;
/
create type esami_sostenutity as object(
	id integer,
	studente ref studentety,
	compito ref compitoty,
	valutazione integer
)final;
/
create type provaty as object(
	id integer,
	studente ref studentety,
	compito ref compitoty,
	domanda ref domandaty,
	risposta ref rispostaty,
	valutazione integer
) final;
/

-- TABELLE
create table insegnamento of insegnamentoty(
	primary key(codice));
/
create table figura of figuraty(
	primary key(id));
/
create table risposta of rispostaty(
	primary key(id));
/
create table domanda of domandaty(
	primary key(id)) 
	nested table risposte store as rispostent_tab, nested table figure store as figurent_tab;
/
create table compito of compitoty(
	primary key(id)) nested table domande store as domandent_tab;
/
create table studente of studentety(
	primary key(matricola));
/
create table esami_sostenuti of esami_sostenutity(
	primary key(id));
/
create table prova of provaty(
	primary key(id));
/

-- SEQUENZE
create sequence figura_seq start with 1;
/
create sequence risposta_seq start with 1;
/
create sequence domanda_seq start with 1;
/
create sequence compito_seq start with 1;
/
create sequence prova_seq start with 1;
/
create sequence esami_sostenuti_seq start with 1;
/

-- TRIGGER
create trigger compito_incr
before insert on compito
for each row
begin
  select compito_seq.nextval into :new.id
  from dual;
end;
/
create trigger domanda_incr
before insert on domanda
for each row
begin
  select domanda_seq.nextval into :new.id
  from dual;
end;
/
create trigger figura_incr
before insert on figura
for each row
begin
  select figura_seq.nextval into :new.id
  from dual;
end;
/
create trigger prova_incr
before insert on prova
for each row
begin
  select prova_seq.nextval into :new.id
  from dual;
end;
/
create trigger risposta_incr
before insert on risposta
for each row
begin
  select risposta_seq.nextval into :new.id
  from dual;
end;
/
create trigger esami_sostenuti_incr
before insert on esami_sostenuti
for each row
begin
  select esami_sostenuti_seq.nextval into :new.id
  from dual;
end;
/
create or replace trigger check_compito
before insert on compito
for each row
begin
    if(:new.insegnamento is null) then
        raise_application_error(-20001,'L''insegnamento non può essere vuoto');
    else
        if(:new.domande.COUNT <> :new.num_domande) then
            raise_application_error(-20002, 'Bisogna inserire un numero di domande pari al campo num_domande');
        end if;
    end if;
end;
/
create or replace trigger check_corretta
before insert on domanda
for each row
when (new.tipo = 'domanda_chiusa')
declare
    new_row domandaty;
    giusta number(1);
    pragma autonomous_transaction;
begin
    new_row := :new.sys_nc_rowinfo$;
    if (new_row.risposte is null) then
        raise_application_error(-20003, 'Ogni domanda deve avere delle risposte.');
    else
        for i in new_row.risposte.first..new_row.risposte.last loop
            select new_row.risposte(i).corretta into giusta from dual;
            if (giusta <> 0 and giusta <> 1) then
                raise_application_error(-20004, 'Inserimento di un valore non consentito per il campo corretta');
            end if;
        end loop;
    end if;
end;
/
create or replace trigger check_insegnamento
before insert or update on insegnamento
for each row
declare
	pragma autonomous_transaction;
begin
    if (:new.numesamisuperati > :new.numesamisostenuti) then
        raise_application_error(-20005, 'Il numero di esami superati non può essere maggiore del numero di esami sostenuti');
	end if;
end;
/
create or replace trigger check_prova
before update on prova
for each row
declare
    new_row provaty;
    val integer;
    dom domanda.id%type;
    punt domanda.punteggio%type;
    pragma autonomous_transaction;
begin
    new_row := :new.sys_nc_rowinfo$;
    select new_row.valutazione, deref(new_row.domanda).id into val, dom from dual;
    select punteggio into punt from domanda where id=dom;
    if(val>punt)then
        raise_application_error(-20006, 'Il voto inserito è maggiore del massimo punteggio attribuibile per questa domanda');
    end if;
end;
/
create or replace trigger update_insegnamento
after insert on esami_sostenuti
for each row
declare
    voto integer;
    cmp compito.id%type;
    ins insegnamento.codice%type;
begin
    select :new.valutazione, deref(:new.compito).id into voto, cmp from dual;
    select deref(c.insegnamento).codice into ins from compito c where c.id=cmp;
    update insegnamento set numesamisostenuti = numesamisostenuti + 1 where codice = ins;
    if (voto > 17) then
        update insegnamento set numesamisuperati = numesamisuperati + 1 where codice = ins;
    end if;
end;
/
create or replace trigger check_esami_sostenuti
before insert on esami_sostenuti
for each row
begin
    if(:new.valutazione > 30 and :new.valutazione < 0) then
        raise_application_error(-20007, 'La valutazione deve essere compresa tra 0 e 30');
    end if;
end;
/
create trigger update_esami_superati
after insert on esami_sostenuti
for each row
declare
    stud studente.matricola%type;
begin
    if(:new.valutazione > 17) then
        select deref(:new.studente).matricola into stud from dual;
        update studente set numesamisuperati = numesamisuperati + 1 where matricola=stud;
    end if;
end;
/
create trigger check_domanda_aperta
before insert on domanda
for each row
when (new.tipo='domanda_aperta')
begin
    if(:new.risposte is not null) then
        raise_application_error(-20008,'Non ci devono essere risposte impostate in una domanda aperta');
    else 
        if(:new.figure.COUNT > 1) then
            raise_application_error(-20009,'Una domanda aperta può avere solo una figura');
        end if;
    end if;
end;
/
create or replace trigger check_ref_esami_sostenuti
before insert on esami_sostenuti
for each row
begin
    if(:new.studente is null) then
        raise_application_error(-20010, 'Lo studente inserito non è valido');
    else
        if(:new.compito is null) then
            raise_application_error(-20011, 'Il compito inserito non è valido');
        end if;
    end if;
end;
/
create trigger check_ref_prova
before insert on prova
for each row
begin
    if(:new.studente is null) then
        raise_application_error(-20012,'Lo studente inserito non è valido');
    else 
        if(:new.compito is null) then
            raise_application_error(-20013, 'Il compito inserito non è valido');
        end if;
    end if;
end;
/
create trigger check_nt_compito
before insert on compito
for each row
begin
    if(:new.domande is null) then
        raise_application_error(-20014, 'Il compito deve avere delle domande');
    end if;
end;
/
create or replace trigger check_duplicati_nt_domande
before insert on domanda
for each row
when (new.tipo = 'domanda_chiusa')
declare 
    new_row domandaty;
    idrispuno risposta.id%type;
    idrispdue risposta.id%type;
begin 
    new_row := :new.sys_nc_rowinfo$;
    for i in new_row.risposte.first..new_row.risposte.last-1 loop
        select deref(new_row.risposte(i).risposte).id into idrispuno from dual;

        for k in i+1..new_row.risposte.last loop
            select deref(new_row.risposte(k).risposte).id into idrispdue from dual;

            if (idrispuno = idrispdue) then
                raise_application_error(-20015, 'La domanda ha risposte duplicate.');
            end if;
        end loop;
    end loop;
end;
/
create or replace trigger check_duplicati_nt_figure
before insert on domanda
for each row
declare 
    new_row domandaty;
    idfigurauno figura.id%type;
    idfiguradue figura.id%type;
begin 
    new_row := :new.sys_nc_rowinfo$;
    for i in new_row.figure.first..new_row.figure.last-1 loop
        select deref(new_row.figure(i).figura).id into idfigurauno from dual;

        for k in i+1..new_row.figure.last loop
            select deref(new_row.figure(k).figura).id into idfiguradue from dual;

            if (idfigurauno = idfiguradue) then
                raise_application_error(-20016, 'La domanda ha figure duplicate.');
            end if;
        end loop;
    end loop;
end;
/
create or replace trigger check_duplicati_nt_compito
before insert on compito
for each row
declare 
    new_row compitoty;
    iddomuno domanda.id%type;
    iddomdue domanda.id%type;
begin 
    new_row := :new.sys_nc_rowinfo$;
    for i in new_row.domande.first..new_row.domande.last-1 loop
        select deref(new_row.domande(i).domanda).id into iddomuno from dual;

        for k in i+1..new_row.domande.last loop
            select deref(new_row.domande(k).domanda).id into iddomdue from dual;

            if (iddomuno = iddomdue) then
                raise_application_error(-20017, 'Il compito ha domande duplicate.');
            end if;
        end loop;
    end loop;
end;
/
create or replace trigger checkuniqueprova
before insert on prova
for each row
declare
    numprove number;
    pragma autonomous_transaction;
begin
    select count(*) into numprove from prova where studente = :new.studente and compito = :new.compito and domanda = :new.domanda;
    if (numprove > 0) then
    raise_application_error(-20018, 'Stai inserendo una prova già esistente');
    end if;
end;
/
create or replace trigger valuta_risposte_chiuse  
before insert on prova
for each row
when (new.domanda.tipo = 'domanda_chiusa')
declare
    dom domanda.id%type;
    risps ref_rispostent;
    risp risposta.id%type;
    risp_stud risposta.id%type;
    punt domanda.punteggio%type;
    bool number(1);
    pragma autonomous_transaction;
begin
    bool := 0;
    select deref(:new.domanda).id, deref(:new.risposta).id into dom, risp_stud from dual;
    select punteggio into punt from domanda where id=dom;
    select d.risposte into risps from domanda d where d.id=dom;
    for i in risps.first..risps.last loop
        select deref(risps(i).risposte).id into risp from dual;
        select risps(i).corretta into bool from dual;
        if(risp_stud = risp) then
            if(bool = 1) then
                :new.valutazione := punt;
            else
                :new.valutazione := 0;
            end if;
        end if;
    end loop;
end;
/

create or replace trigger check_domande_prova
before insert on prova
for each row
declare
    iddom domanda.id%type;
    idcomp compito.id%type;
    doms ref_domandent;
    dom domanda.id%type;
    bool number(1);
    pragma autonomous_transaction;
begin
    bool :=0;
    select deref(:new.compito).id, deref(:new.domanda).id into idcomp, iddom from dual;
    select c.domande into doms from compito c where c.id=idcomp;
    for i in doms.first..doms.last loop
        select deref(doms(i).domanda).id into dom from dual;
        if (dom=iddom) then
            bool := 1;
        end if;
    end loop;
    if (bool = 0) then
        raise_application_error(-20019, 'La domanda non è presente in questo compito');
    end if;
end;
/
create or replace trigger check_risposte_prova
before insert on prova
for each row
declare
    iddom domanda.id%type;
    idrisp risposta.id%type;
    risps ref_rispostent;
    risp risposta.id%type;
    bool number(1);
    pragma autonomous_transaction;
begin
    bool :=0;
    select deref(:new.risposta).id, deref(:new.domanda).id into idrisp, iddom from dual;
    select c.risposte into risps from domanda c where c.id=iddom;
    for i in risps.first..risps.last loop
        select deref(risps(i).risposte).id into risp from dual;
        if (risp=idrisp) then
            bool := 1;
        end if;
    end loop;
    if (bool = 0) then
        raise_application_error(-20020, 'La risposta non è possibile per questa domanda');
    end if;
end;
/

-- QUERY
insert into insegnamento values(1,'basi di dati',0,0);
insert into insegnamento values(2,'programmazione 2',0,0);
insert into insegnamento values(3,'analisi 1',0,0);
/
insert into figura values(1,'un orso');
insert into figura values(1, 'un cane');
insert into figura values(1, 'un gatto');
/
insert into risposta select risposta_chiusaty('pippo') from dual; 
insert into risposta select risposta_chiusaty('pluto') from dual; 
insert into risposta select risposta_chiusaty('paperino') from dual;
insert into risposta select risposta_chiusaty('3') from dual;
insert into risposta select risposta_chiusaty('4') from dual;
insert into risposta select risposta_chiusaty('5') from dual;
/
insert into risposta select risposta_apertaty('la seconda guerra mondiale') from dual;
insert into risposta select risposta_apertaty('1914-1918') from dual;
insert into risposta select risposta_apertaty('Leopardi era un grande scrittore') from dual;
/
insert into domanda select domanda_chiusaty(
'chi è il cane della disney?', 5,
ref_figurent(
    ref_figurety((select ref(f) from figura f where f.id=1))),
ref_rispostent(
    ref_rispostety((select treat(ref(r) as ref risposta_chiusaty) from risposta r where r.id=1), 0),
    ref_rispostety((select treat(ref(r) as ref risposta_chiusaty) from risposta r where r.id=2), 1),
    ref_rispostety((select treat(ref(r) as ref risposta_chiusaty) from risposta r where r.id=3), 0))) from dual;
insert into domanda select domanda_chiusaty(
'Quanti figli aveva D''Annunzio?', 5,
ref_figurent(
    ref_figurety((select ref(f) from figura f where f.id=-1))), -- ho messo null
ref_rispostent(
    ref_rispostety((select treat(ref(r) as ref risposta_chiusaty) from risposta r where r.id=4), 0),
    ref_rispostety((select treat(ref(r) as ref risposta_chiusaty) from risposta r where r.id=5), 1),
    ref_rispostety((select treat(ref(r) as ref risposta_chiusaty) from risposta r where r.id=6), 0))) from dual;
/
insert into domanda select domanda_apertaty('Cosa è successo negli anni 1939-1945?', 10,
ref_figurent(
    ref_figurety((select ref(f) from figura f where f.id=-1))) -- ho messo null
) from dual;
/
insert into compito values(1,'malerba',(select ref(i) from insegnamento i where i.codice=2),to_date('2010-07-07','yyyy-mm-dd'),2,
ref_domandent(
    ref_domandety((select ref(d) from domanda d where d.id=1)),
    ref_domandety((select ref(d) from domanda d where d.id=2))));
insert into compito values(1,'ceci',(select ref(i) from insegnamento i where i.codice=1),to_date('2010-07-07','yyyy-mm-dd'),3,
ref_domandent(
    ref_domandety((select ref(d) from domanda d where d.id=1)),
    ref_domandety((select ref(d) from domanda d where d.id=2)),
    ref_domandety((select ref(d) from domanda d where d.id=3))));
/
insert into studente values(1, 'mastroscianni',0);
insert into studente values(2,'lorusso',0);
/
insert into esami_sostenuti values(1,(select ref(s) from studente s where s.matricola=1), (select ref(c) from compito c where c.id=1),27);
insert into esami_sostenuti values(1,(select ref(s) from studente s where s.matricola=1), (select ref(c) from compito c where c.id=2),28);
insert into esami_sostenuti values(1,(select ref(s) from studente s where s.matricola=1), (select ref(c) from compito c where c.id=2),17);
insert into esami_sostenuti values(1,(select ref(s) from studente s where s.matricola=2), (select ref(c) from compito c where c.id=1),30);
/
insert into prova values(1, (select ref(s) from studente s where s.matricola=1), (select ref(c) from compito c where c.id=1),
(select ref(d) from domanda d where d.id=1),(select ref(r) from risposta r where r.id=2),null);    
insert into prova values(1, (select ref(s) from studente s where s.matricola=1), (select ref(c) from compito c where c.id=1),
(select ref(d) from domanda d where d.id=2),(select ref(r) from risposta r where r.id=4),null);   
insert into prova values(1, (select ref(s) from studente s where s.matricola=2), (select ref(c) from compito c where c.id=1),
(select ref(d) from domanda d where d.id=1),(select ref(r) from risposta r where r.id=1),null);  
insert into prova values(1, (select ref(s) from studente s where s.matricola=2), (select ref(c) from compito c where c.id=1),
(select ref(d) from domanda d where d.id=2),(select ref(r) from risposta r where r.id=6),null);
/

-- QUERY INDICE
select id, deref(studente).cognome, deref(deref(compito).insegnamento).nome, valutazione from esami_sostenuti where deref(studente).matricola=1;  