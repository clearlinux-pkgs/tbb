#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tbb
Version  : 2019.u9
Release  : 27
URL      : https://github.com/01org/tbb/archive/2019_U9/tbb-2019.U9.tar.gz
Source0  : https://github.com/01org/tbb/archive/2019_U9/tbb-2019.U9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: tbb-lib = %{version}-%{release}
Requires: tbb-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
Patch1: build.patch
Patch2: timestamp.patch
Patch3: defaults.patch

%description
.. contents::
Introduction
------------
Many developers use CMake to manage their development projects, so the Threading Building Blocks (TBB)
team created the set of CMake modules to simplify integration of the TBB library into a CMake project.
The modules are available starting from TBB 2017 U7 in `<tbb_root>/cmake <https://github.com/01org/tbb/tree/tbb_2017/cmake>`_.

%package dev
Summary: dev components for the tbb package.
Group: Development
Requires: tbb-lib = %{version}-%{release}
Provides: tbb-devel = %{version}-%{release}
Requires: tbb = %{version}-%{release}
Requires: tbb = %{version}-%{release}

%description dev
dev components for the tbb package.


%package lib
Summary: lib components for the tbb package.
Group: Libraries
Requires: tbb-license = %{version}-%{release}

%description lib
lib components for the tbb package.


%package license
Summary: license components for the tbb package.
Group: Default

%description license
license components for the tbb package.


%prep
%setup -q -n tbb-2019_U9
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570897969
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
make  %{?_smp_mflags}  DEFAULTFLAGS="$CFLAGS"


%install
export SOURCE_DATE_EPOCH=1570897969
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tbb
cp LICENSE %{buildroot}/usr/share/package-licenses/tbb/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/serial/tbb/parallel_for.h
/usr/include/serial/tbb/tbb_annotate.h
/usr/include/tbb/aggregator.h
/usr/include/tbb/aligned_space.h
/usr/include/tbb/atomic.h
/usr/include/tbb/blocked_range.h
/usr/include/tbb/blocked_range2d.h
/usr/include/tbb/blocked_range3d.h
/usr/include/tbb/blocked_rangeNd.h
/usr/include/tbb/cache_aligned_allocator.h
/usr/include/tbb/combinable.h
/usr/include/tbb/compat/condition_variable
/usr/include/tbb/compat/ppl.h
/usr/include/tbb/compat/thread
/usr/include/tbb/compat/tuple
/usr/include/tbb/concurrent_hash_map.h
/usr/include/tbb/concurrent_lru_cache.h
/usr/include/tbb/concurrent_map.h
/usr/include/tbb/concurrent_priority_queue.h
/usr/include/tbb/concurrent_queue.h
/usr/include/tbb/concurrent_set.h
/usr/include/tbb/concurrent_unordered_map.h
/usr/include/tbb/concurrent_unordered_set.h
/usr/include/tbb/concurrent_vector.h
/usr/include/tbb/critical_section.h
/usr/include/tbb/enumerable_thread_specific.h
/usr/include/tbb/flow_graph.h
/usr/include/tbb/flow_graph_abstractions.h
/usr/include/tbb/flow_graph_opencl_node.h
/usr/include/tbb/global_control.h
/usr/include/tbb/index.html
/usr/include/tbb/internal/_aggregator_impl.h
/usr/include/tbb/internal/_allocator_traits.h
/usr/include/tbb/internal/_concurrent_queue_impl.h
/usr/include/tbb/internal/_concurrent_skip_list_impl.h
/usr/include/tbb/internal/_concurrent_unordered_impl.h
/usr/include/tbb/internal/_deprecated_header_message_guard.h
/usr/include/tbb/internal/_flow_graph_async_msg_impl.h
/usr/include/tbb/internal/_flow_graph_body_impl.h
/usr/include/tbb/internal/_flow_graph_cache_impl.h
/usr/include/tbb/internal/_flow_graph_impl.h
/usr/include/tbb/internal/_flow_graph_indexer_impl.h
/usr/include/tbb/internal/_flow_graph_item_buffer_impl.h
/usr/include/tbb/internal/_flow_graph_join_impl.h
/usr/include/tbb/internal/_flow_graph_node_impl.h
/usr/include/tbb/internal/_flow_graph_node_set_impl.h
/usr/include/tbb/internal/_flow_graph_nodes_deduction.h
/usr/include/tbb/internal/_flow_graph_streaming_node.h
/usr/include/tbb/internal/_flow_graph_tagged_buffer_impl.h
/usr/include/tbb/internal/_flow_graph_trace_impl.h
/usr/include/tbb/internal/_flow_graph_types_impl.h
/usr/include/tbb/internal/_mutex_padding.h
/usr/include/tbb/internal/_node_handle_impl.h
/usr/include/tbb/internal/_range_iterator.h
/usr/include/tbb/internal/_tbb_hash_compare_impl.h
/usr/include/tbb/internal/_tbb_strings.h
/usr/include/tbb/internal/_tbb_trace_impl.h
/usr/include/tbb/internal/_tbb_windef.h
/usr/include/tbb/internal/_template_helpers.h
/usr/include/tbb/internal/_warning_suppress_disable_notice.h
/usr/include/tbb/internal/_warning_suppress_enable_notice.h
/usr/include/tbb/internal/_x86_eliding_mutex_impl.h
/usr/include/tbb/internal/_x86_rtm_rw_mutex_impl.h
/usr/include/tbb/iterators.h
/usr/include/tbb/machine/gcc_arm.h
/usr/include/tbb/machine/gcc_generic.h
/usr/include/tbb/machine/gcc_ia32_common.h
/usr/include/tbb/machine/gcc_itsx.h
/usr/include/tbb/machine/ibm_aix51.h
/usr/include/tbb/machine/icc_generic.h
/usr/include/tbb/machine/linux_common.h
/usr/include/tbb/machine/linux_ia32.h
/usr/include/tbb/machine/linux_ia64.h
/usr/include/tbb/machine/linux_intel64.h
/usr/include/tbb/machine/mac_ppc.h
/usr/include/tbb/machine/macos_common.h
/usr/include/tbb/machine/mic_common.h
/usr/include/tbb/machine/msvc_armv7.h
/usr/include/tbb/machine/msvc_ia32_common.h
/usr/include/tbb/machine/sunos_sparc.h
/usr/include/tbb/machine/windows_api.h
/usr/include/tbb/machine/windows_ia32.h
/usr/include/tbb/machine/windows_intel64.h
/usr/include/tbb/memory_pool.h
/usr/include/tbb/mutex.h
/usr/include/tbb/null_mutex.h
/usr/include/tbb/null_rw_mutex.h
/usr/include/tbb/parallel_do.h
/usr/include/tbb/parallel_for.h
/usr/include/tbb/parallel_for_each.h
/usr/include/tbb/parallel_invoke.h
/usr/include/tbb/parallel_reduce.h
/usr/include/tbb/parallel_scan.h
/usr/include/tbb/parallel_sort.h
/usr/include/tbb/parallel_while.h
/usr/include/tbb/partitioner.h
/usr/include/tbb/pipeline.h
/usr/include/tbb/queuing_mutex.h
/usr/include/tbb/queuing_rw_mutex.h
/usr/include/tbb/reader_writer_lock.h
/usr/include/tbb/recursive_mutex.h
/usr/include/tbb/runtime_loader.h
/usr/include/tbb/scalable_allocator.h
/usr/include/tbb/spin_mutex.h
/usr/include/tbb/spin_rw_mutex.h
/usr/include/tbb/task.h
/usr/include/tbb/task_arena.h
/usr/include/tbb/task_group.h
/usr/include/tbb/task_scheduler_init.h
/usr/include/tbb/task_scheduler_observer.h
/usr/include/tbb/tbb.h
/usr/include/tbb/tbb_allocator.h
/usr/include/tbb/tbb_config.h
/usr/include/tbb/tbb_disable_exceptions.h
/usr/include/tbb/tbb_exception.h
/usr/include/tbb/tbb_machine.h
/usr/include/tbb/tbb_profiling.h
/usr/include/tbb/tbb_stddef.h
/usr/include/tbb/tbb_thread.h
/usr/include/tbb/tbbmalloc_proxy.h
/usr/include/tbb/tick_count.h
/usr/lib64/libtbb.so
/usr/lib64/libtbbmalloc.so
/usr/lib64/libtbbmalloc_proxy.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtbb.so.2
/usr/lib64/libtbbmalloc.so.2
/usr/lib64/libtbbmalloc_proxy.so.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tbb/LICENSE
