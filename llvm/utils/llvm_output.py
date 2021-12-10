import llvmlite.binding as llvm
from llvmlite.binding import ExecutionEngine, ModuleRef

# All these initializations are required for code generation!
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()  # yes, even this one


def create_execution_engine() -> ExecutionEngine:
    """
    Create an ExecutionEngine suitable for JIT code generation on
    the host CPU.  The engine is reusable for an arbitrary number of
    modules.
    """
    # Create a target machine representing the host
    target = llvm.Target.from_default_triple()
    target_machine = target.create_target_machine()
    # And an execution engine with an empty backing module
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, target_machine)
    return engine


def compile_ir(engine: ExecutionEngine, llvm_ir: str) -> ModuleRef:
    """
    Compile the LLVM IR strings with the given engine.
    The compiled module object is returned.
    """
    # Create a LLVM module object from the IR
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    # Now add the module and make sure it is ready for execution
    engine.add_module(mod)
    engine.finalize_object()
    engine.run_static_constructors()
    return mod


def write_ir(filename: str, llvm_ir: str) -> None:
    with open(filename, 'w') as out:
        # target triple = x86_64-pc-linux-gnu
        llvm_ir = llvm_ir.replace('unknown-unknown-unknown', 'x86_64-linux-gnu')
        # llvm_ir = llvm_ir.replace('unknown-unknown-unknown', 'i386-win32')
        out.write(llvm_ir)
